# Carmenta: Goddess of Childbirth and Prophecy

## Building

```
Docker build -t carmenta:latest .
```

## First Time Setup

Run

```
$ ./install.sh
```

This will install `chromedriver` and set up your `~/.bash_profile` to export the `CHROMEDRIVER` environment variable.

## Running

```
Docker run -p 5000:5000 carmenta:latest
```

## Testing

```
Running on 127.0.0.1:5000
```
