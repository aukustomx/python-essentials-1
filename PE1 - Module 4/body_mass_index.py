def body_mass_index(weight, height):

    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return
    
    return weight / height ** 2

print("BMI =", body_mass_index(0, 0))

ONE_LB_IN_KG = 0.45359237

def lb_to_kg(lbs):
    return lbs * ONE_LB_IN_KG

ONE_FEET_TO_METERS = 0.3048
ONE_INCH_TO_METERS = 0.0254

def ft_and_inch_to_meters(ft, inch = 0):
    return ft * ONE_FEET_TO_METERS + inch * ONE_INCH_TO_METERS

print("BMI =", body_mass_index(weight = lb_to_kg(176), height = ft_and_inch_to_meters(5, 7)))
