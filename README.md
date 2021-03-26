# Rest_News

# Install

git clone https://github.com/Nikolai-veb/Rest_News.git

cd Rest_News

docker-compose build

docker-compose up

docker-compose exec web python manage.py collectstatic

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py cretesuperuser

# Routs

lockalhost/articles/ - list articles

lockalhost/articles/article/article_slug - single article

lockalhost/articles/add_article/ - adds new article, available only for authorized users

lockalhost/articles/delete_article/article_slug - delete article, available only for authorized users

lockalhost/articles/update_article/article_slug - update article, available only for authorized users

lockalhost/auth/token/login/ - add token

lockalhost/auth/token/logout - delete token

lockalhost/auth/users/ - sing up

lockalhost/auth/users/activation/ - activation new user







