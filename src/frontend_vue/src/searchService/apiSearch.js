export default function parseParams(params) {
    const keys = Object.keys(params)
    let options = ''
  
    keys.forEach((key) => {
      const isParamTypeObject = typeof params[key] === 'object'
      const isParamTypeArray = isParamTypeObject && params[key].length >= 0
  
      if (!isParamTypeObject) {
        options += `${key}=${params[key]}&`
      }
  
      if (isParamTypeObject && isParamTypeArray) {
        params[key].forEach((element) => {
          options += `${key}=${element}&`
        })
      }
    })
  
    return options ? options.slice(0, -1) : options
  }

export const apiURL = () => {return 'http://127.0.0.1:8000'}