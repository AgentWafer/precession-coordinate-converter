from osgeo import ogr
import math
import shutil


def rotate_coordinates(phi_deg, lambda_deg, alpha_deg, beta_deg):
    phi_rad = math.radians(phi_deg)
    lambda_rad = math.radians(lambda_deg)
    alpha_rad = math.radians(alpha_deg)
    beta_rad = math.radians(beta_deg)

    # Cartesian coordinates
    x = math.cos(phi_rad) * math.cos(lambda_rad)
    y = math.cos(phi_rad) * math.sin(lambda_rad)
    z = math.sin(phi_rad)

    # Rotate by alpha (Z-axis)
    x_prime = x * math.cos(alpha_rad) - y * math.sin(alpha_rad)
    y_prime = x * math.sin(alpha_rad) + y * math.cos(alpha_rad)
    z_prime = z

    # Rotate by beta (Y-axis)
    x_double_prime = x_prime * math.cos(beta_rad) + z_prime * math.sin(beta_rad)
    y_double_prime = y_prime
    z_double_prime = -x_prime * math.sin(beta_rad) + z_prime * math.cos(beta_rad)

    # Clamp z to avoid numerical errors
    z_double_prime_clamped = max(min(z_double_prime, 1.0), -1.0)
    phi_prime_rad = math.asin(z_double_prime_clamped)

    # Handle poles
    if abs(phi_prime_rad) > math.pi / 2:
        phi_prime_rad = math.copysign(math.pi - abs(phi_prime_rad), phi_prime_rad)
        lambda_prime_rad = math.atan2(y_double_prime, x_double_prime) + math.pi
    else:
        lambda_prime_rad = math.atan2(y_double_prime, x_double_prime)

    # Normalize longitude
    lambda_prime_deg = (math.degrees(lambda_prime_rad) + 180) % 360 - 180
    phi_prime_deg = math.degrees(phi_prime_rad)

    return phi_prime_deg, lambda_prime_deg

alpha_deg = 40
beta_deg = -30

driver = ogr.GetDriverByName("ESRI Shapefile")
datasource = driver.Open("../old/ne_110m_populated_places.shp", 0)
layer = datasource.GetLayer()

shutil.copytree("../old", "../new")
driver_new = ogr.GetDriverByName("ESRI Shapefile")
datasource_new = driver_new.Open("../new/ne_110m_populated_places.shp", 0)

coords_init = []
for feature in layer:
    geom = feature.GetGeometryRef()
    if geom is not None:
        coords_init.append((round(geom.GetX(),2), round(geom.GetY(),2)))

coords_trans = []
for i in range(len(coords_init) - 1):
    phi_deg, lambda_deg = rotate_coordinates(coords_init[i][1], coords_init[i][0], alpha_deg, beta_deg)
    coords_trans.append((lambda_deg, phi_deg))

for feature in layer:
    geom = feature.GetGeometryRef()
    geom.SetPoint(0, lambda_deg, phi_deg)

for i in range(len(coords_init) - 1):
    print(f"Old: {round(coords_init[i][0], 2)}E, {round(coords_init[i][1], 2)}N; New: {round(coords_trans[i][0], 2)}E, {round(coords_trans[i][1], 2)}N")
