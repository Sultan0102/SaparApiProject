import TokenService from "./TokenService";
import Api from "./Api"
import AuthService from "./AuthService";


const setup = (store, router, axiosInstance) => {
  axiosInstance.interceptors.request.use(
    (config) => {
      const token = TokenService.getLocalAccessToken();
      if (token) {
        config.headers["Authorization"] = 'Bearer ' + token; 
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
      debugger;
      if (originalConfig.url !== "login/" && err.response) {
        // Access Token was expired
        
        if(err.response.status == 401) {
          // redirect to login?
          if(err.response.data.error_code == "not_authenticated") {
            router.push("/login")
            return Promise.reject(err)
          }

          if(err.response.data.error_code == "refresh_token_invalid") {
            store.dispatch('logout')
            router.push("/home")
            return Promise.reject(err)
          }

          if(err.response.data.error_code == "invalid_token" || err.response.data.error_code == 'token_not_valid') {
            debugger;
            originalConfig._retry = true;
            const res = await TokenService.refreshToken().then((response)=>{
              TokenService.updateLocalAccessToken(response.data.access)
              return axiosInstance(originalConfig)
            });

            }
          }
        }

        // if(err.response.status == 500) {
        //   router.push("/")          
        // }

        if (err.response.status == 403) {
          // redirect to page which says that user has no access 
          router.push("/forbidden")
        }

        
       return Promise.reject(err); 
      }
  );
};

export default setup;