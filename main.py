api_demo.py
import urllib.request, json

def get_joke():
    with urllib.request.urlopen(
        "<https://official-joke-api.appspot.com/random_joke>"
    ) as resp:
        data = json.load(resp)
    return f"{data['setup']} – {data['punchline']}"

if __name__ == "__main__":
    print("Here's a joke for you:")
    print(get_joke())
python3 api_demo.py 
```jsx
api_demo.js
fetch("<https://official-joke-api.appspot.com/random_joke>")
  .then(r => r.json())
  .then(j => console.log(`${j.setup} – ${j.punchline}`))
  .catch(console.error);
```

- [ ]  Run: `node api_demo.js`
### `post_demo.py` (Python)

```python
# post_demo.py
import urllib.request, json

payload = json.dumps({
    "name": "Intern",
    "task": "API demo"
}).encode("utf-8")

req = urllib.request.Request(
    "<https://httpbin.org/post>",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    result = json.load(resp)

print("Response from httpbin.org:")
print(json.dumps(result, indent=2))
```

- [ ]  Run: `python3 post_demo.py` 
```jsx
("<https://httpbin.org/post>", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Intern", task: "API demo" })
})
  .then(r => r.json())
  .then(console.log)
  .catch(console.error);
```

- [ ]  Run: `node post_demo.js`
- [ ]  `git add post_demo.py` *(or `post_demo.js`)*
- [ ]  `git commit -m "Add POST request demo (httpbin echo)"`
- [ ]  `git push`
- [ ]  `git checkout main`
- [ ]  `git pull` *Get the latest `main`*
- [ ]  `git merge intern‑tasks` *Integrate your work*
- [ ]  Resolve any conflicts (there should be none)
- [ ]  `git push`
- [ ]  `git branch -d intern‑tasks`
- [ ]  `git push origin 