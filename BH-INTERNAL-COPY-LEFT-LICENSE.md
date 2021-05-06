
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">



  <title>Initiating SAML single sign-on</title>
  <meta http-equiv="refresh" content="0;url=https://fss.gecompany.com/fss/idp/SSO.saml2?PartnerSpId=https://github.build.ge.com&amp;RelayState=mvaY4l0d6-xyL7Ezwho1p6eavIsl3sYqM4HJKqFuWGtTNQLSHFytISgQrcSYjRYzpp5RyFGFw79DP_BHtXXhuf_GQm1j1Ia7jNt-QxRzXBw&amp;SAMLRequest=fZJBj5swEIXv%2ByuQ7wFMQgArJGI3qhppu0FL2kMvlTHjxBLY1DZp99%2BvYRN1q3ZzsjR%2Bb%2FS%2BmVltfnetdwZthJI5wn6INuu7laFd25NisCf5DD8HMNZzOmnI9JGjQUuiqBGGSNqBIZaRqvjySCI%2FJL1WVjHVoneW2w5qDGjrAiBvt83Rj3SOaZzMI77APIuSjOMl4JSGeJFgjhscp2yxrGucwBxnFAPOkqzhjDIIF2kaJ66NMQPspLFU2hxFYYRnYTwLlwe8IHFMouV35H27QrsIyNs6RiGpnSona3tDgoAb4x%2BBqa6n8sV371gJRNMHVbX3R7BoU1JtJeiq3zX51XcU9jTUfj2ItnENRueYqXSg4gw54rQ1gLzyMql7IRshj7eHVL%2BJDPl8OJSzcl8dkFdcB%2FegpBk6lwL0WTD4%2Bvz4B%2BI%2FYYIxesDeTGg9rZtMM9PrG7ZV8F54OZInl3S3LVUr2ItXtK369aCBWkdp9eAgPyndUfsxG%2FbxVBHNjE9SMkjTAxNcQIOCSzgH2IiR1HhPyt6Dk8JHi3WCvdzrglvQf2tiEoaTxrUN%2Fr3x9d0r&amp;SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&amp;Signature=kXlJ%2FoolAMBas%2Fs8%2FNFL5id%2BrXGrmDCTZUQIgYEwIjqCdIHdeQj4i%2FVbSoFBhnbyc8IWJmzS4cpz%2FcU7%2BRwLJ4yVrW0CyUFPGHJbF9%2BNC4bB7pFV%2FcblumCTaXrTIYGYLEhVWZMl88mGOTEIjWJvlxkpL2%2B0S90H7cTkAdgKGJYM6RoeO6RgmgysdQ%2F3BqCvCr4GsxVN5%2FXVWtWqsYi06DPyAgRhjIlPEX6XiodU%2BW40mA8dnU7fJRD%2B9jNrjxUFMWt9ePQP%2FtN6e0dSc6nMlzDNmF1KfFHcNb794lYJRZTzE9ZFgSze%2FWwgsW8CeHFsAg5KkGDzHQ9xkFO5%2FgmUCAI5J6Kw3L6sl1PGn7qbZGB2jPZ459xXMpFpqSr3jX4rGoNGsfxyv%2B1QgeRpb4w1F%2BUbTbWuUMuoWRYiTq%2Bl19ptRDJVBjkTJ7r3FYRzgHavc00cyV1IDayenNUxNtuNB9gChPsIHK9x49hUBvZ6HW1JXcbD5I0zJmz4Dv5WRYrK5kFPdTxqXkRyf1tuZZ80ENhZFV0N94AWn%2BXQOYyZIpoXprY1%2BUGQeYecb54cP%2FhsSs3281lVCemhvLiLiW0%2F6XlWZwwvPnKhFCd7Ibb5z0Gite4qt0rPz5o6dCg1Uyv5jzg3khbss4jp4DDuESSKICVzRUTLiA%2F0sBLdUhI4uCw%3D" data-url="https://fss.gecompany.com/fss/idp/SSO.saml2?PartnerSpId=https://github.build.ge.com&amp;RelayState=mvaY4l0d6-xyL7Ezwho1p6eavIsl3sYqM4HJKqFuWGtTNQLSHFytISgQrcSYjRYzpp5RyFGFw79DP_BHtXXhuf_GQm1j1Ia7jNt-QxRzXBw&amp;SAMLRequest=fZJBj5swEIXv%2ByuQ7wFMQgArJGI3qhppu0FL2kMvlTHjxBLY1DZp99%2BvYRN1q3ZzsjR%2Bb%2FS%2BmVltfnetdwZthJI5wn6INuu7laFd25NisCf5DD8HMNZzOmnI9JGjQUuiqBGGSNqBIZaRqvjySCI%2FJL1WVjHVoneW2w5qDGjrAiBvt83Rj3SOaZzMI77APIuSjOMl4JSGeJFgjhscp2yxrGucwBxnFAPOkqzhjDIIF2kaJ66NMQPspLFU2hxFYYRnYTwLlwe8IHFMouV35H27QrsIyNs6RiGpnSona3tDgoAb4x%2BBqa6n8sV371gJRNMHVbX3R7BoU1JtJeiq3zX51XcU9jTUfj2ItnENRueYqXSg4gw54rQ1gLzyMql7IRshj7eHVL%2BJDPl8OJSzcl8dkFdcB%2FegpBk6lwL0WTD4%2Bvz4B%2BI%2FYYIxesDeTGg9rZtMM9PrG7ZV8F54OZInl3S3LVUr2ItXtK369aCBWkdp9eAgPyndUfsxG%2FbxVBHNjE9SMkjTAxNcQIOCSzgH2IiR1HhPyt6Dk8JHi3WCvdzrglvQf2tiEoaTxrUN%2Fr3x9d0r&amp;SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&amp;Signature=kXlJ%2FoolAMBas%2Fs8%2FNFL5id%2BrXGrmDCTZUQIgYEwIjqCdIHdeQj4i%2FVbSoFBhnbyc8IWJmzS4cpz%2FcU7%2BRwLJ4yVrW0CyUFPGHJbF9%2BNC4bB7pFV%2FcblumCTaXrTIYGYLEhVWZMl88mGOTEIjWJvlxkpL2%2B0S90H7cTkAdgKGJYM6RoeO6RgmgysdQ%2F3BqCvCr4GsxVN5%2FXVWtWqsYi06DPyAgRhjIlPEX6XiodU%2BW40mA8dnU7fJRD%2B9jNrjxUFMWt9ePQP%2FtN6e0dSc6nMlzDNmF1KfFHcNb794lYJRZTzE9ZFgSze%2FWwgsW8CeHFsAg5KkGDzHQ9xkFO5%2FgmUCAI5J6Kw3L6sl1PGn7qbZGB2jPZ459xXMpFpqSr3jX4rGoNGsfxyv%2B1QgeRpb4w1F%2BUbTbWuUMuoWRYiTq%2Bl19ptRDJVBjkTJ7r3FYRzgHavc00cyV1IDayenNUxNtuNB9gChPsIHK9x49hUBvZ6HW1JXcbD5I0zJmz4Dv5WRYrK5kFPdTxqXkRyf1tuZZ80ENhZFV0N94AWn%2BXQOYyZIpoXprY1%2BUGQeYecb54cP%2FhsSs3281lVCemhvLiLiW0%2F6XlWZwwvPnKhFCd7Ibb5z0Gite4qt0rPz5o6dCg1Uyv5jzg3khbss4jp4DDuESSKICVzRUTLiA%2F0sBLdUhI4uCw%3D">
  <meta name="viewport" content="width=device-width">
  <link crossorigin="use-credentials" media="all" integrity="sha512-UzMqFF3u6q+PIf7vRROKCCcSAIYk0CGPD1MvMAnv0X7Pqxc6MTt+l1mXE6StaVvPg+m/XgXexi1uO8P/zszHgA==" rel="stylesheet" href="https://github.build.ge.com/assets/frameworks-53332a145deeeaaf8f21feef45138a08.css" />
  <link crossorigin="use-credentials" media="all" integrity="sha512-OjLzwi/p8mjjfWtWCrPLbeZem4jzl/IWUvdseQTXqLcLUjAnF7rGsfFxWUfDRURNW4YCSes9IpkKDcgJ7VTUfg==" rel="stylesheet" href="https://github.build.ge.com/assets/github-3a32f3c22fe9f268e37d6b560ab3cb6d.css" />



  <link rel="mask-icon" href="https://github.build.ge.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.build.ge.com/favicons/favicon-ent.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.build.ge.com/favicons/favicon-ent.svg">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body>
    
  
<div class="container-md px-3">
  <div class="blankslate mt-5">
    <svg class="octicon octicon-shield-lock blankslate-icon" height="32" viewBox="0 0 24 24" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M12.077 2.563a.25.25 0 00-.154 0L3.673 5.24a.249.249 0 00-.173.237V10.5c0 5.461 3.28 9.483 8.43 11.426a.2.2 0 00.14 0c5.15-1.943 8.43-5.965 8.43-11.426V5.476a.25.25 0 00-.173-.237l-8.25-2.676zm-.617-1.426a1.75 1.75 0 011.08 0l8.25 2.675A1.75 1.75 0 0122 5.476V10.5c0 6.19-3.77 10.705-9.401 12.83a1.699 1.699 0 01-1.198 0C5.771 21.204 2 16.69 2 10.5V5.476c0-.76.49-1.43 1.21-1.664l8.25-2.675zM13 12.232A2 2 0 0012 8.5a2 2 0 00-1 3.732V15a1 1 0 102 0v-2.768z"></path></svg>


    <h3 class="mb-1">You are being redirected to your identity provider in order to authenticate.</h3>


  
    <p>
      If your browser does not redirect you back, please <a id="redirect" href="https://fss.gecompany.com/fss/idp/SSO.saml2?PartnerSpId=https://github.build.ge.com&amp;RelayState=mvaY4l0d6-xyL7Ezwho1p6eavIsl3sYqM4HJKqFuWGtTNQLSHFytISgQrcSYjRYzpp5RyFGFw79DP_BHtXXhuf_GQm1j1Ia7jNt-QxRzXBw&amp;SAMLRequest=fZJBj5swEIXv%2ByuQ7wFMQgArJGI3qhppu0FL2kMvlTHjxBLY1DZp99%2BvYRN1q3ZzsjR%2Bb%2FS%2BmVltfnetdwZthJI5wn6INuu7laFd25NisCf5DD8HMNZzOmnI9JGjQUuiqBGGSNqBIZaRqvjySCI%2FJL1WVjHVoneW2w5qDGjrAiBvt83Rj3SOaZzMI77APIuSjOMl4JSGeJFgjhscp2yxrGucwBxnFAPOkqzhjDIIF2kaJ66NMQPspLFU2hxFYYRnYTwLlwe8IHFMouV35H27QrsIyNs6RiGpnSona3tDgoAb4x%2BBqa6n8sV371gJRNMHVbX3R7BoU1JtJeiq3zX51XcU9jTUfj2ItnENRueYqXSg4gw54rQ1gLzyMql7IRshj7eHVL%2BJDPl8OJSzcl8dkFdcB%2FegpBk6lwL0WTD4%2Bvz4B%2BI%2FYYIxesDeTGg9rZtMM9PrG7ZV8F54OZInl3S3LVUr2ItXtK369aCBWkdp9eAgPyndUfsxG%2FbxVBHNjE9SMkjTAxNcQIOCSzgH2IiR1HhPyt6Dk8JHi3WCvdzrglvQf2tiEoaTxrUN%2Fr3x9d0r&amp;SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&amp;Signature=kXlJ%2FoolAMBas%2Fs8%2FNFL5id%2BrXGrmDCTZUQIgYEwIjqCdIHdeQj4i%2FVbSoFBhnbyc8IWJmzS4cpz%2FcU7%2BRwLJ4yVrW0CyUFPGHJbF9%2BNC4bB7pFV%2FcblumCTaXrTIYGYLEhVWZMl88mGOTEIjWJvlxkpL2%2B0S90H7cTkAdgKGJYM6RoeO6RgmgysdQ%2F3BqCvCr4GsxVN5%2FXVWtWqsYi06DPyAgRhjIlPEX6XiodU%2BW40mA8dnU7fJRD%2B9jNrjxUFMWt9ePQP%2FtN6e0dSc6nMlzDNmF1KfFHcNb794lYJRZTzE9ZFgSze%2FWwgsW8CeHFsAg5KkGDzHQ9xkFO5%2FgmUCAI5J6Kw3L6sl1PGn7qbZGB2jPZ459xXMpFpqSr3jX4rGoNGsfxyv%2B1QgeRpb4w1F%2BUbTbWuUMuoWRYiTq%2Bl19ptRDJVBjkTJ7r3FYRzgHavc00cyV1IDayenNUxNtuNB9gChPsIHK9x49hUBvZ6HW1JXcbD5I0zJmz4Dv5WRYrK5kFPdTxqXkRyf1tuZZ80ENhZFV0N94AWn%2BXQOYyZIpoXprY1%2BUGQeYecb54cP%2FhsSs3281lVCemhvLiLiW0%2F6XlWZwwvPnKhFCd7Ibb5z0Gite4qt0rPz5o6dCg1Uyv5jzg3khbss4jp4DDuESSKICVzRUTLiA%2F0sBLdUhI4uCw%3D">click here</a> to continue.
    </p>



</div></div>


  </body>
</html>
