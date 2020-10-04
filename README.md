# gitlab-pipelines-not-passing

This script checks GitLab pipelines statuses for configured repositories and only outputs ones that are not passing.  It was designed to be used with [py3status][0].  

```console
$ python gitlab-pipelines-not-passing.py
glib, jakrevo
```

## py3status configuration

```
i3block gitlab {
    command = "echo GitLab failures $(python /path/to/gitlab-pipelines-not-passing.py) 2> /dev/null"
    interval = 3600
}
```

[0]: https://github.com/ultrabug/py3status
