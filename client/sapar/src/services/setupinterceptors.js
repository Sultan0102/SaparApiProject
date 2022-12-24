import TokenService from "./TokenService";
import Api from "./Api"


const setup = (store, axiosInstance) => {
  axiosInstance.interceptors.request.use(
    (config) => {
      const token = TokenService.getLocalAccessToken();
      if (token) {
        config.headers["Authorization"] = 'Bearer ' + token; // for Node.js Express back-end
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  axiosInstance.interceptors.response.use(
    (res) => {
      return res;
    },
    async (err) => {
      const originalConfig = err.config;

      if (originalConfig.url !== "/auth/login/" && err.response) {
        // Access Token was expired
        if (err.response.status === 401 && !originalConfig._retry) {
          originalConfig._retry = true;
          try {
            const rs = await Api.auth.post("refresh/", {
              refresh: TokenService.getLocalRefreshToken(),
            });

            const { access } = rs.data;

            store.dispatch('auth/refreshToken', access);
            TokenService.updateLocalAccessToken(access);

            return axiosInstance(originalConfig);
          } catch (_error) {
            return Promise.reject(_error);
          }
        }

        if (err.response.status == 403 && err.response.data == 'Token is invalid or expired') {
            store.dispatch('logout');
        }
      }

      return Promise.reject(err);
    }
  );
};

export default setup;