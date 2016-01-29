# portlandpython.org

![Travis CI Build Status](https://travis-ci.org/portlandpython/portlandpython.org.svg?branch=master)

New Portland Python Website

### Delpoy notes
A couple notes to get up and running on a new heroku app.

#### Setting the heroku buildpack
Since a `package.json` and a `requirements.txt` exist in the repo, Heroku gets a little
confused and thinks the repo is both a Node.js and Python app. Heroku will default to Node.js in this
case and we must either tell Heroku that this is a python app.  
If we want to install JS dependencies from the `pagackage.json`, then we'll need to set up a multi-buildpack.

```console
remote: -----> Warning: Multiple default buildpacks reported the ability to handle this app. The first buildpack in the list below will be used.
remote:        Detected buildpacks: Node.js, Python
remote:        See https://devcenter.heroku.com/articles/buildpacks#buildpack-detect-order
remote: -----> Node.js app detected
remote:
remote: -----> Creating runtime environment
```

And in the server log we can see that gunicorn isn't installed:

```
2016-01-29T18:09:07.351681+00:00 app[web.1]: bash: gunicorn: command not found
```

The buildpack can be set by the command: `heroku buildpacks:set heroku/python` or in a multi-buildpack scenario
we can add additional buildpacks with the comand: `heroku buildpacks:add --index 1 heroku/nodejs`

See: https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app


#### Requires config
You must add the following config variables to get the app up and running:

```
SECRET_KEY
```

#### Deploying Branches
Local branches can be deployed to heroku too!

`git push heroku fix/16-config-for-heroku:master`

