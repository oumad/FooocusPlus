import os
import sys
import fooocus_version

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
os.chdir(root)

old_version = version.get_fooocusplus_ver()

print('Welcome to FooocusPlus: checking for updates...')
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

new_version = version.get_fooocusplus_ver()
if new_version != old_version:
    print('Updated FooocusPlus from ,old_version, to ,new_version')
    print()

from launch import *
