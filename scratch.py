from conf_git import GIT_COMMIT_ARGS, REMOTE_URL, checkout_repo
from run import run
import logging as log

checkout_repo(REMOTE_URL)
# cmd = ["git", "commit", "--date","96 days ago","-m", "removed unnecessary files" , "--allow-empty"]
cmd = ["git", "commit", "--date=96 days ago","-m", "removed unnecessary files" , "--allow-empty"]


print(f"cmd is {cmd}")
res, err = run(cmd)
log.info(res)
log.error(err)
