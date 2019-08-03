# Carmenta: Goddess of Childbirth and Prophecy

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
