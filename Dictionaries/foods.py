fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour, yellow, citrus fruit',
         'grape': 'a small, sweet fruit grown in bunches',
         'lime': 'a sour, green citrus fruit'}

veg = {'brussel sprouts': "every child's favorite",
       'broccoli': 'good with some cheese/soy sauce',
       'spinach': 'throw some salsa in there, quit complaining'}

# Note: .update() won't return any values, this won't work:
# print(veg.update(fruit))

veg.update(fruit)
print(veg)
