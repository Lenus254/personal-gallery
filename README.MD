# PERSONAL GALLERY 
## Author  
  
>[Linus cheruiyot](https://github.com/Lenus254)  
  
# Description  
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  
##  Live Link  
 Click [View Site](https://lenisgallery.herokuapp.com/)  to visit the site
  
 
## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo and share.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```
 https://github.com/Lenus254/personal-gallery
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Personal-gallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  

 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Running tests 
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.2](https://docs.djangoproject.com/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* Sometimes copy button fails to work 
  

  
## License 
License:MIT
-Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.)  
* Copyright (c) 2022 **Linus Cheruiyot**