import Api from "./Api"


class TokenService {
      getLocalRefreshToken() {
        return JSON.parse(localStorage.getItem("refreshToken"));
        
      }
    
      getLocalAccessToken() {
        return JSON.parse(localStorage.getItem("accessToken"));

      }
    
      updateLocalAccessToken(token) {
        localStorage.setItem("accessToken", JSON.stringify(token));
      }

      updateLocalRefreshToken(token) {
        localStorage.setItem("refreshToken", JSON.stringify(token));
      }
      
    
      getUser() {
        return JSON.parse(localStorage.getItem("user"));
      }
    
      setUser(user) {
        console.log(JSON.stringify(user));
        localStorage.setItem("user", JSON.stringify(user));
      }
    
      removeUser() {
        localStorage.removeItem("user");
      }

      removeTokens() {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");

      }

      refreshToken() {
        return Api.auth.post("refresh/", {
          "refresh": this.getLocalRefreshToken()
        });
      }
}


export default new TokenService();