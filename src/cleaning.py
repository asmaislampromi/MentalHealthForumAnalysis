import pandas as pd
import re
import os

def load_and_clean_all_reddit_posts(folder_path):
    """
    Loads, concatenates, and cleans all Reddit *_posts.csv files in the folder.
    """
    all_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith('_posts.csv')
    ]
    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        if 'content' in df.columns:
            df['content'] = df['content'].astype(str).str.lower()
            df['content'] = df['content'].apply(lambda x: re.sub(r'http\S+', '', x))
            df['content'] = df['content'].apply(lambda x: re.sub(r'[^a-z0-9\s]', '', x))
            df['content'] = df['content'].fillna('')
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
        if 'author' in df.columns:
            df['author'] = df['author'].fillna('unknown')
        df_list.append(df)
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df
def load_and_clean_all_reddit_comments(folder_path):
    """
    Loads, concatenates, and cleans all Reddit *_comments.csv files in the folder.
    """
    import pandas as pd
    import re
    import os

    all_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith('_comments.csv')
    ]
    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        if 'content' in df.columns:
            df['content'] = df['content'].astype(str).str.lower()
            df['content'] = df['content'].apply(lambda x: re.sub(r'http\S+', '', x))
            df['content'] = df['content'].apply(lambda x: re.sub(r'[^a-z0-9\s]', '', x))
            df['content'] = df['content'].fillna('')
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
        if 'author' in df.columns:
            df['author'] = df['author'].fillna('unknown')
        df_list.append(df)
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df
