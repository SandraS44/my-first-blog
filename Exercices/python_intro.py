def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
hi("Ola")


def ho(rachel):
	print('Hi ' + rachel + '!')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for rachel in girls:
	hi(rachel)
	print('Next girl')

ho(rachel)
django-admin.py
