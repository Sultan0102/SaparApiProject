import devConfig from './dev.env'
import prodConfig from './prod.env'

const config = null;

if (process.env.NODE_ENV == 'development') {
    config = devConfig
} else {
    config = prodConfig
}

export default config;