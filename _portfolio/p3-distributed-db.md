---
title: "Job Posting Distributed Database Management System"
excerpt: "<span>- Distributed Database Management System, Data Scraping, Custom Hash Partitioning</span><br/>- Python, Django, MySQL, Selenium WebDriver, BeautifulSoup<br/><br/>Developed a Django-based Distributed Database Management System for job postings from scratch, utilizing a custom hash function to partition data across 3 MySQL databases. The dataset was obtained by scraping LinkedIn Jobs using Selenium WebDriver for automated navigation and BeautifulSoup for HTML parsing.<br/><img src='/images/django.PNG'>"
collection: portfolio
---

Key accomplishments:
---
- Designed and implemented a Django-based Distributed Database Management System from scratch, optimizing data handling for job postings through efficient, custom data partitioning across 3 MySQL databases.
- The hash function for partitioning was calculated by adding up the ASCII values of all characters in the title, then applying a modulo operation by 3 (to match the number of databases) to determine the target database (<a href="https://pages.cs.wisc.edu/~siff/CS367/Notes/hash.html" target="_blank">inspiration from here</a>). This approach distributes data evenly and reduces retrieval time by ensuring balanced database loads.
- Data scraping from LinkedIn Jobs using Selenium WebDriver for navigation and BeautifulSoup for HTML parsing, simulating a robust and comprehensive job postings dataset.

You can find the full project on <a href="https://github.com/kikossik/Job-Posting-Distributed-Database-Management-System" target="_blank">GitHub</a>, where you can fork or set it up on your local machine. Comprehensive documentation, along with the Python script for scraping job posting data using from LinkedIn.