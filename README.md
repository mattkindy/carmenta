# Carmenta: Goddess of Childbirth and Prophecy

This project is an experimental attempt to create a tool to automate sourcing by using a sample of "known good" candidates and use 
information from LinkedIn / social networks to identify other potentially good candidates for a given party

## Startup

Make sure you have docker installed, then run:

```
docker-compose up --build
```

## Testing

```
Navigate to 0.0.0.0:5000
```

Example curl request to check if a user would be a good Praetorian fit
```curl -X POST -H "Content-Type: application/json" -d
'{"username":"anna.pobletts@praetorian.com","password":"<password>", "link":"https://www.linkedin.com/in/dr-jared-demott-vdalabs/"}' http://0.0.0.0:5000/api/cluster/```

### UI Development
1. make sure you have python, npm, and pip installed on your machine.
2. cd into `web/templates/carmenta`
3. Run `npm install` if you haven't yet
4. Run `npm start`
