
const saveStorage = function (key, item){
    sessionStorage.setItem(key, JSON.stringify(item));
};

const getStorage = function (key){
    if(sessionStorage.getItem(key)){
        const data = JSON.parse(sessionStorage.getItem(key))
        return data
    }else{
        return null;
    }
}

const clearStorage = function(key){
    sessionStorage.removeItem(key)
}

export {saveStorage, getStorage, clearStorage};