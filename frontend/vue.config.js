// vue.config.js
// const path = require("path");

module.exports = {
    // options...
    devServer: {
        proxy: {
            '^/api': {
                target: 'http://localhost:5000',
                ws: true,
                changeOrigin: true
            },
        }
    },
    // publicPath: process.env.NODE_ENV === 'production'
    //     ? '/static'
    //     : '/',
    // The app will be deployed to the backend/static directory when
    // npm run build
    // outputDir: path.resolve(__dirname, "../../backend/static"),
    // assetsDir: "."

}