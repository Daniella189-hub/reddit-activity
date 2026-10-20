#!/usr/bin/python3
import requests

Info = {"User-Agent": "python:ALU-practice:v1.0 (by /u/HourPerception623)"}
query = "music"

def get(url):
    ready = requests.get(url, headers=Info, timeout=10)
    print("Status Code:", ready.status_code)
    if ready.status_code != 200:
        print("Blocked or failed. Reddit said:", ready.text[:150])
        raise SystemExit
    return ready.json()

# displaying the name, description and subscribers
results = get(f"https://www.reddit.com/subreddits/search.json?q={query}&limit=1")
sub = results["data"]["children"][0]["data"]

name = sub["display_name"]
print("Name:", name) 
print("subscribers:", sub[subscribers])
print("description:", sub["public_subscription"])
print

# 2.rules
rules = get(f"https://www.reddit.com/r/{name}/about/rules.json")["rules"]
print("\nRules:")
for rule in rules:
    print("-", rule["short_name"])

#3. 10 post
posts = get(f"https://www.reddit.com/r/{name}/new.json?limit=10")["data"]["children"]
print("\n10 newest posts:")
for post in posts:
    print("-", post["data"]["title"])
