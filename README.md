# scrapy_spider
REQUIRED LIBRARIES:
 -- pip install scrapy
 -- pip install django
 -- pip install djangorestframework
 -- pip install pyyaml
 -- pip install drf-yasg


SETPS FOR RUNNING THE PROJECT

1. In parliment_spider/pipelines.py switch the connection to the db.sqlite3 path.
2. cd to the django project directory and migrate the model so the table gets created.
3. Run the scrapy spider from the scrapy shell 
4. Run the django rest app 
