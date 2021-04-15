import requests

host = ''

def testAuth():
    url = 'http://srmbp158.t.xgimi.com/apis/permission/user/auth'
    header = {'Cookie':'UM_distinctid=17631e5616d923-095aa600bba5fc-4313f6a-1fa400-17631e5616ec5e; GM_TOKEN=lP4WEeyU9rfwjqkaQ9ys0l8N52oJoCH99FUjTvxwNilij3sID%2Fj5cjTTJyxDfT8O4uXwr1RLOYLzT5JqSKnp9vPUdnQKiG8g4PzUbnmbpjck4wtvtTy6I5Kb%2F7jJaWUsK8jGpEoz%2Fd1pWdk0Kjx2j5oEGGUrEC1ZHa5a7Wpz8VuGG18D2hHOZ9EsaCMQciee%2BHOJZ1cqxmzf%2FywIPe0XSw%3D%3D; uid=14630; CNZZDATA1279498227=30232056-1607581494-null%7C1608168884; passToken=MTAyMGVYR1kwRGhkT1R0NDh0S3E5SFFpSkREWDlrWlJMYmpmQXdTckVmdWN2enZPdy9mQmJFakdlRVBsczNMNmM2NTVkeTV6ZHNMUlI3VUh1M1Y3OEc4YTRMSllaOGptOHFRSk5MUUhzT1Z4c3lIaGdpTGtrOG1DVnNzUjdhTUxaMFVOS2laQ2JXL2xuK3RVTVZTOXdiSjYrZk5PNUVaU0wwLzEzRzQ3SW1pUDN5cEROcjFXZ2FuZC9FVkxXa1lLZS9GcU50a2l5dG5ZVjhZ'}
    r = requests.get(url,headers=header)
    message = r.json()
    print(message)

testAuth()