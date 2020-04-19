# Dotabase frontend

> A Vue.js project
> 同时使用了Vuex，Vuex-Router，Vuex-Loader

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# PS: 如果报错说缺少XXX包，就执行 npm install XXX。 例如如果程序不认识devx包，npm install devx

# build for production with minification
npm run build
```

## 组织架构

components: 一些页面组件
|__ Hero.vue: 主页上的英雄头像

layouts: 布局
|__ Main.vue: 最外层的通用框架

mock: 模拟测试用的数据，数据结构应与后端保持一致

pages: 每个不同的页面
|__ 404.vue
|__ App.vue     逻辑上的主页面
|__ Home.vue    主页（一堆英雄头像）
|__ Detail.vue  英雄详情页
|__ Login.vue   登录页面

store: 可以理解为全局变量池

main.js: 主脚本（路由信息直接写在了这里）
