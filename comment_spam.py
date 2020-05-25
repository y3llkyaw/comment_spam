import json,facebook,requests
print(('\033[32;1m'+'|------------------------------|').center(44))
print(('\033[32;1m'+'  |---------'+'\033[31;1mComment Spam'+'\033[32;1m'+'---------|').center(44))
print(('\033[32;1m'+'|------------------------------|').center(44))
print('CODED BY *YHK* '.center(35))
token = input("Enter Access Token: ")

try:
    graph = facebook.GraphAPI(token)
    me = graph.get_object('me')
    print('Account: '+me['name'])
    target = input("Enter Target Friend's Name: ")
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    result = json.loads(friends.text)
    # print(result)
    for i in result['data']:
        if i['name'] == target:
            id = i['id']
            user = graph.get_object(id)
            posts = graph.get_connections(user['id'], "posts")
            for p in posts['data']:
                print('')
                if 'message' not in p.keys():
                    print(('\033[31;1mNo Captions\033[32;1m'))
                else:
                    print('Caption: '+p['message'])
                print('ID:' + p['id'])
            pid = input("Frined's Post ID: ")
            message = input('Enter comment: ')
            q = int(input('Enter Quantity of Comment: '))

            for x in range(q):
                graph.put_comment(pid,message)
            print('Success')
        else:
           print('\033[31;1m[*]'+'Friend Not Found')

except:
    print("SOMETHING WENT WORNG")
