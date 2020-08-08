![Deploy](https://github.com/tim-hub/Pocket2Wordpress/workflows/Deploy/badge.svg)![CI](https://github.com/tim-hub/Pocket2Wordpress/workflows/CI/badge.svg)

A small personal tool to post articles from pocket to wordpress automatically.



# Getting Started
**Intergration will be [start weekly](.github/workflows/deploy.yml)**

## Setup Environment Variables
- copy [.end.default](.env.default) paste as .env
- set up your env variables there
    - [get pocket api key](https://getpocket.com/developer/docs/authentication)
    - [get wp application password](https://wordpress.org/plugins/application-passwords/) not required if generate markdowns

## Run Locally
- pipenv install -d
- pipenv run cli.py MD
    - MD for generating markdown files  (dist folder)
    - WP will save posts to wordpress

> Lambda Handler `app/app.handler` when you trigger on AWS lambda





## Deploy

Two ways:
- Lambda + CloudWatch
- Github action cron job



# About

This project is inspired by [Mabbs](https://github.com/Mabbs/MayxDaily) 
1. He/She used a PHP script to fetch content from API
    - save content as markdown
    - public to github page
2. Travis CI to trigger the script automatically


## Pocket2Wordpress

![](https://raw.githubusercontent.com/tim-hub/picgo-pictures-sample2/master/public/images20200728211825.png)

1. Instead of PHP script, Python is used here for 
    - fetch [content from Pocket](https://getpocket.com/developer/)
    - format content and render them to HTML in string
    - post them to wordpress blog ( [Authentication Plugin is required](https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/) on wordpress side )
2. travis => Github action, which is doing the same job
    - and Lambda+Cloud Watch Cron can be used here too
3. post post content to wordpress



## Development
- [AWS SAM AWS Lambda Function get started/contributing](./CONTRIBUTING.md)
- [License](./LICENSE)

### todo weekly
- [ ] split read and unread
- [x] enable flake8 and clean up
- [ ] add bing daily image
- [ ] support hacker news api too


