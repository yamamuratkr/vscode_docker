# vscode_docker
VS Code上でDjango+Nginx+Postresql+Pgadminのコンテナを起動するためのDocker資材

## 前提
- ローカルの端末にDockerコンテナの開発環境を作ることを目的としている
- Docker Desktopが端末にインストールされていること
- VS Codeが端末にインストールされていること
- 以下のVS Code 拡張機能がインストールされていること
  - Dev Containers
  - Remote - SSH: Editing Configuration Files

## 起動方法
- Docker Desktopを起動
- 以下のコマンドでリポジトリをクローン
```
git clone https://github.com/yamamuratkr/vscode_docker.git
```
- VS Codeでcloneした`vscode_docker/docker/webapp`を開く
- 「コンテナで再度開く」をクリックするとコンテナが起動する

![image](https://github.com/user-attachments/assets/af3de7e8-5aa4-4527-95c8-91bcc09cb3c2)

![スクリーンショット 2024-10-04 14 06 12](https://github.com/user-attachments/assets/66a44400-2242-4670-8442-be34e78cab94)

- Docker Desktopを確認するとコンテナが起動している様子が確認できる

![image](https://github.com/user-attachments/assets/35bfdb60-6508-42c4-83ad-97094262539c)

## Djangoの動作確認
- ブラウザで以下のURLを入力してDjangoアプリに接続確認
  - URL: http://localhost:1317

![image](https://github.com/user-attachments/assets/183fbc34-0e9e-4075-be2d-cc365200e97d)

## Pgadminへの接続
- ブラウザで以下のURLを入力してPgadminに接続確認
  - URL: http://localhost:8888

![image](https://github.com/user-attachments/assets/87e66625-75ea-4fda-ba42-b3726bb7614b)

- メールアドレスとパスワードは`docker-compose.yaml`の`enviorment`に記載されている
- 適宜変更して再度コンテナを起動すると新しいメールアドレスとパスワードでログインできる

![image](https://github.com/user-attachments/assets/e8653eea-4d07-459a-805d-b8424e57e707)

## 資材について
### フォルダ階層
```
vscode_docker
├── docker
│   ├── nginx         # nginx の Docker コンテナ用資材
│   ├── postgresql    # postgresql の Docker コンテナ用資材
│   │   └── init      # DB初期化用SQL（初回コンテナ起動時に実行される）
│   └── webapp        # Django の Docker コンテナ用資材
└── src
    ├── Webapp
    │   └── webapp
    │       └── sample  # Django 資材の格納場所
    └── nginx
        └── static      # Django に反映される静的資材の格納場所
            ├── css
            ├── images
            └── js      
```

### Nginxの設定ファイル
- `vscode_docker/docker/nginx`に`default.conf`と`nginx.conf`が格納されている
- Nginx の設定が記述されている。これらを編集してコンテナを再起動することで Nginx の独自カスタマイズが可能となる。

### Djangoを育てる
- コンテナが起動できたらあとは好きにDjangoを育てていけば良い
- `python manage.py startapp xxxx`で新しいアプリを作成できる
- viewsを作成することで新しい機能を追加する
- CSSやjavascript, 画像は`vscode_docker/src/nginx/static`に置くとHTMLで呼び出すことが可能になる
- HTMLは`vscode_docker/src/Webapp/webapp/sample/sample_app/templates`に配置し、views.pyで定義した関数でレンダリングして呼び出すことで画面が表示される。
