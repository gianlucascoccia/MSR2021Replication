# %% Imports

import pandas as pd
import numpy as np

# %% Load repositories data 

nw_repos = pd.read_excel('../data/raw/DesktopWebApps.xlsx', 'NWjs_repo_info')
el_repos = pd.read_excel('../data/raw/DesktopWebApps.xlsx', 'Electron_repo_info')

# %% execute filtering of repos

nw_repos = nw_repos[nw_repos.isOnGit == 1]
el_repos = el_repos[el_repos.isOnGit == 1]

# Remove repositories with less than 10 commits
nw_repos = nw_repos[nw_repos['commits'] > 10]
el_repos = el_repos[el_repos['commits'] > 10]

# Remove repositories with less than 8 weeks lifetime
nw_repos = nw_repos[(nw_repos['lastCommitDate'] - nw_repos['firstCommitDate']) > 4838400]
el_repos = el_repos[(el_repos['lastCommitDate'] - el_repos['firstCommitDate']) > 4838400]

# %% load commits

nw_commits = pd.read_csv('../data/raw/NWjs_commits.tsv', sep='\t')
el_commits = pd.read_csv('../data/raw/Electron_commits.tsv', sep='\t')

# merge commits with repos

nw_commits = pd.merge(nw_commits, nw_repos['folderName'], on='folderName')
el_commits = pd.merge(el_commits, el_repos['folderName'], on='folderName')

# %% load issues

nw_issues = pd.read_excel('../data/raw/DesktopWebApps.xlsx', 'NWjs_issues')
el_issues = pd.read_excel('../data/raw/DesktopWebApps.xlsx', 'Electron_issues')

# merge with repos

nw_issues = pd.merge(nw_issues, nw_repos['folderName'], on='folderName')
el_issues = pd.merge(el_issues, el_repos['folderName'], on='folderName')

# Remove issues in language != eng
nw_issues = nw_issues[nw_issues['language'] == 'en']
el_issues = el_issues[el_issues['language'] == 'en']

# compute issue count for each repo
nwic = nw_issues.groupby(['folderName']).size().reset_index(name='issueCount')
elic = el_issues.groupby(['folderName']).size().reset_index(name='issueCount')

nw_repos = nw_repos.merge(nwic, on='folderName', how='outer').fillna(0, downcast='infer')
el_repos = el_repos.merge(elic, on='folderName', how='outer').fillna(0, downcast='infer')

# %% load dependencies
    
nw_deps = pd.read_excel('../data/raw/DesktopWebApps.xlsx', 'NWjs_dependencies')
el_deps = pd.read_excel('../data/raw/DesktopWebApps.xlsx', 'Electron_dependencies')

# merge dependencies with repos

nw_deps = pd.merge(nw_deps, nw_repos['folderName'], on='folderName')
el_deps = pd.merge(el_deps, el_repos['folderName'], on='folderName')

# %% load issue comments

nw_comments = pd.read_csv('../data/raw/NWjs_comments.tsv', sep='\t')
el_comments = pd.read_csv('../data/raw/Electron_comments.tsv', sep='\t')

# merge issue comments with repos
nw_comments = pd.merge(nw_comments, nw_repos['folderName'], on='folderName')
el_comments = pd.merge(el_comments, el_repos['folderName'], on='folderName')

# strip symbols from comments


# remove duplicate comments
nw_comments['commentId'] = nw_comments.apply(lambda row: row['folderName'] + '_' + str(row['issueId']) + '_' + str(row['commentNumber']), axis=1)
nw_comments = nw_comments.drop_duplicates(subset=['body','commentId'], keep='first')
el_comments['commentId'] = el_comments.apply(lambda row: row['folderName'] + '_' + str(row['issueId']) + '_' + str(row['commentNumber']), axis=1)
el_comments = el_comments.drop_duplicates(subset=['body','commentId'], keep='first')


# %% Store cleaned and processed data

# Commits
el_commits.to_csv('../data/processed/el_commits.csv')
nw_commits.to_csv('../data/processed/nw_commits.csv')

# Issues
el_issues.to_csv('../data/processed/el_issues.csv')
nw_issues.to_csv('../data/processed/nw_issues.csv')

# Repositories
el_repos.to_csv('../data/processed/el_repos.csv')
nw_repos.to_csv('../data/processed/nw_repos.csv')

# Dependencies
el_deps.to_csv('../data/processed/el_deps.csv')
nw_deps.to_csv('../data/processed/nw_deps.csv')

# Comments
nw_comments.to_csv('../data/processed/nw_comments.csv')
el_comments.to_csv('../data/processed/el_comments.csv')

# %%
