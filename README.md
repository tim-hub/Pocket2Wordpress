![Python application](https://github.com/tim-hub/Pocket2Wordpress/workflows/Python%20application/badge.svg)

A small personal tool to post articles from pocket to wordpress automatically.

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



# Getting Started

## Deploy

Two ways:
- Lambda + CloudWatch
- Github action cron



## Development
- [AWS SAM AWS Lambda Function get started/contributing](./CONTRIBUTING.md)
- [License](./LICENSE)

### todo weekly
- [ ] split read and unread
- [ ] enable flake8 and clean up
- [ ] add bing daily image
- [ ] support hacker news api too


