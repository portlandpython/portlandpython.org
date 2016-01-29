# portlandpython.org

![Travis CI Build Status](https://travis-ci.org/portlandpython/portlandpython.org.svg?branch=master)

New Portland Python Website

### Delpoy notes
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

The buildpack can be set by the command: `heroku buildpacks:set heroku/python` or in a multi-buildpack scenario
we can add additional buildpacks with the comand: `heroku buildpacks:add --index 1 heroku/nodejs`

See: https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app