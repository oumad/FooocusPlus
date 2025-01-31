import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
os.chdir(root)

fooocusplus_ver = ''
def get_fooocusplus_ver():
    global fooocusplus_ver, commit_id
    if not fooocusplus_ver:
        fooocusplus_log = os.path.abspath(f'./fooocusplus_log.md')
        if os.path.exists(fooocusplus_log):
            with open(fooocusplus_log, "r", encoding="utf-8") as log_file:
                line = log_file.readline().strip()
                while line:
                    if line.startswith("# "):
                        break
                    line = log_file.readline().strip()                
        else:
            line = '0.9.0'
        fooocusplus_ver = line.strip('# ')
        if commit_id:
            fooocusplus_ver += f'.{commit_id}'
    return fooocusplus_ver

print('Welcome to FooocusPlus ,fooocusplus_ver,: checking for updates...')
print()

try:
    import pygit2
    pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)

    repo = pygit2.Repository(os.path.abspath(os.path.dirname(__file__)))

    branch_name = repo.head.shorthand
    
    remote_name = 'origin'
    remote = repo.remotes[remote_name]

    remote.fetch()

    origin_name = 'main'
    main_name = 'main'
    local_branch_ref = f'refs/heads/{branch_name}'
    if branch_name != main_name:
        print(f'Ready to checkout {branch_name}')
        branch_name = main_name
        local_branch_ref = f'refs/heads/{branch_name}'
        new_branch = repo.lookup_branch(branch_name)
        repo.checkout(new_branch)

    local_branch = repo.lookup_reference(local_branch_ref)
    local_commit = repo.revparse_single(local_branch_ref)

    remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
    remote_commit = repo.revparse_single(remote_reference)

    merge_result, _ = repo.merge_analysis(remote_commit.id)

    if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
        print(f'{branch_name if branch_name!="main" else "FooocusPlus"}: Already up-to-date, {str(local_commit.id)[:7]}')
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
        local_branch.set_target(remote_commit.id)
        repo.head.set_target(remote_commit.id)
        repo.checkout_tree(repo.get(remote_commit.id))
        repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)
        print(f'{branch_name if branch_name!="main" else "FooocusPlus"}: Fast-forward merge, {str(local_commit.id)[:7]} <- {str(remote_commit.id)[:7]}')
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
        print(f'{branch_name if branch_name!="main" else "FooocusPlus"}: Update failed - Did you modify any files? {str(local_commit.id)[:7]} <- {str(remote_commit.id)[:7]}')
except Exception as e:
    print(f'{branch_name if branch_name!="main" else "FooocusPlus"}: Update failed.')
    print(str(e))

new_version = get_fooocusplus_ver()
if new_version != fooocusplus_ver:
    print('Updated FooocusPlus from ,fooocusplus_ver, to ,new_version')
    print()

from launch import *
