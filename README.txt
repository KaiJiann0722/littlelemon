The app restaurant also the API app, please check the urls file and test the API.
The username and password are saved in the account.txt file.
Im using third party MYSQL so all you need to do is just run and test the code, thank you.
**Note the url:
http://127.0.0.1:8000/restaurant/ -> this serve the static files 
http://127.0.0.1:8000/restaurant/menu/ -> get all the list of the, or use post method to insert new
http://127.0.0.1:8000/restaurant/menu/1 -> update or delete the item
http://127.0.0.1:8000/restaurant/booking/tables/ -> get the info of booking tables, 
                                                        must login(authentication)
                                                        
All url login or get token from djoser, you can take the account from account.txt 
    or login as superuser and create a new account.
