// vue.config.js
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
    publicPath: process.env.NODE_ENV === 'production'
        ? '/static'
        : '/'
}