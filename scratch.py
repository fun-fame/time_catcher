from conf_git import GIT_COMMIT_ARGS, REMOTE_URL, checkout_repo
from run import run
import logging as log

checkout_repo(REMOTE_URL)
cmd = ["git", "commit",GIT_COMMIT_ARGS ,"-m", "removed unnecessary files"]

print(f"cmd is {cmd}")
res, err = run(cmd)
log.info(res)
log.error(err)
