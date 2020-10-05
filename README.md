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

## Why not?

Why not use the py3status [GitLab module][1]?

The module requires a token, and I did not fell like creating accounts just for this purpose.

Why parse the pipeline status badge svg files instead of using the [GitLab API][2]?

At the time, it was way easier.

[0]: https://github.com/ultrabug/py3status
[1]: https://py3status.readthedocs.io/en/latest/modules.html#gitlab
[2]: https://docs.gitlab.com/ee/api/README.html
