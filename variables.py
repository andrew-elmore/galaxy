inhabited_stars_data = {
    'exponent': 1,
    'multiple': 1,
    'constant': 0
}
expantion_inclanation_data = {
    'exponent': 1,
    'multiple': 1,
    'constant': 0
}
year_data = {
    'exponent': 1,
    'multiple': 0.5,
    'constant': 0
}

multiple = 1
constant = 0
divisor = 1

def create_expantion_capacity(inhabited_stars, expantion_inclanation, year):
    inhabited_stars_data['value'] = inhabited_stars
    expantion_inclanation_data['value'] = expantion_inclanation
    year_data['value'] = year


    inhabited_stars_res = (inhabited_stars_data.get('value') **
                           inhabited_stars_data.get('exponent')) + inhabited_stars_data.get('constant')

    expantion_inclanation_res = (expantion_inclanation_data.get('value') **
                                 expantion_inclanation_data.get('exponent')) + expantion_inclanation_data.get('constant')
    year_res = (year_data.get('value') **
                year_data.get('exponent')) + year_data.get('constant')
    return (((inhabited_stars_res + expantion_inclanation_res + year_res) * multiple) + constant)/divisor
    pass
