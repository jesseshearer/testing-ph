try:
  ph = int(input('Pick a number between 0 and 14 to test your PH '))

  if ph > 14:
    print('Please pick a number between 0 and 14 next time.')

  elif ph < 0:
    print('Please pick a number between 0 and 14 next time.')

  elif ph < 7:
    print('Acidic')
  
  elif ph > 7:
    print('Basic')

  else:
    print('Neutral')
  
except ValueError:
  print('Please pick a number between 0 and 14 next time.')
