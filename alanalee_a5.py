cuisine = {'Chinese': ['Mapo Tofu', 'House Fried Rice', 'Xiaolongbao'],
           'Mexican': ['Huevos Rancheros', 'Burrito', 'Pozole'],
           'Italian': ['Mushroom Risotto','Fettuccine Alfredo', 'Cheese Pizza']};

print ("""You are eligible for a free 3 course meal from a restaurant in your area!
First, start by choosing a cuisine from the options below.
-----
1 : Chinese
2 : Mexican
3 : Italian
-----""")



while True:
        
        def answer(cuisine):
                print('Enter the name of the cuisine you want: ')
                print('You chose ' + cuisine + '! Here are your dishes:')
                answer(Chinese)
        if answer == 'Chinese':
                print('You chose Chinese! Here are your dishes:')
                for item in cuisine['Chinese']:
                        print(item)
        if answer == 'Mexican':
                print('You chose Mexican! Here are your dishes:')
                for item in cuisine['Mexican']:
                        print(item)
        if answer == 'Italian':
                print('You chose Italian! Here are your dishes:')
                for item in cuisine['Italian']:
                        print(item)
                        
        while True:
                answer = input('Would you like to choose a different option? Yes | No: ')
                if answer == 'No':
                        print('Enjoy your meal!')
                        bool_app = True
                        break
                elif answer == 'Yes':
                        bool_app = False
                        break
                        
        if bool_app : break
        if not bool_app: continue
