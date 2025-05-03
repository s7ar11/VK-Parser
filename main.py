import os
from dotenv import load_dotenv
from tqdm import tqdm
from vk_api import VKParser
from utils import save_to_csv
from config import GROUPS

load_dotenv()

def main():
    if not GROUPS:
        raise ValueError("Список групп не задан в .env (VK_GROUPS)")

    os.makedirs("output", exist_ok=True)

    vk_parser = VKParser(os.getenv("VK_TOKEN"))
    
    # Сбор постов
    posts = []
    for group in tqdm(GROUPS, desc="Парсинг групп"):
        posts.extend(vk_parser.get_posts(group))
    save_to_csv(posts, "output/posts.csv")
    
    # Сбор комментариев
    comments = []
    for post in tqdm(posts, desc="Парсинг комментариев"):
        comments.extend(vk_parser.get_comments(post.group_id, post.post_id))
    save_to_csv(comments, "output/comments.csv")

if __name__ == "__main__":
    main()