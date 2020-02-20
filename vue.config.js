module.exports = {
    chainWebpack: config => {
        config.module.rules.delete("eslint");
    },

    // publicPath: "/igo-tools/"
};
