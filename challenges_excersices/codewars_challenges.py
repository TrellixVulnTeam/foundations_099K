# CODEWARS, Count the smiley faces!

# Description:
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)

array = [':D', 'GD', ':)', ':D', ';-D', ':~)']

def count_smileys(arr):
	valid_eyes = [':', ';',]
	valid_nose = ['-', '~']
	valid_mouth = [')', 'D']

	smiley_counter = 0
	print('', )
	print('  ', 'Here are the valid smileys: ')

	for smiley in arr:
		if len(smiley) == 3:
				if smiley[0] in valid_eyes:
					if smiley[1] in valid_nose:
						if smiley[2] in valid_mouth:
							smiley_counter += 1
							print('-> ', smiley)
		elif len(smiley) == 2:
				if smiley[0] in valid_eyes and smiley[1] in valid_mouth:
					smiley_counter += 1
					print('-> ', smiley)
	                    
		else:
			print('0')

	print('---------------')
	print(' ', 'There are', smiley_counter, 'in that array.')

count_smileys(array)


					
