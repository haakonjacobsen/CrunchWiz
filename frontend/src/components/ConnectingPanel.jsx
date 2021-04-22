import React, { useState } from 'react';
import './ConnectingPanel.css';
import PropTypes from 'prop-types';

export default function ConnectingPanel({ errorMsg, isLoading, connectWebsocket }) {
  const [ipPart, changeIP] = useState('');
  const [portPart, changePort] = useState('');

  return (
    <div className="Connecting-panel">
      <h1 className="Connecting-panel-title"> Connect to server </h1>
      <div className="Connecting-input">
        <div className="SVG-container">
          <svg viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M27.5789 20.8607C27.5789 21.1647 27.4704 21.4256 27.2539 21.6422C27.0369 21.8587 26.7714 21.9672 26.4583 21.9672C26.1447 21.9672 25.8792 21.8587 25.6627 21.6422C25.4462 21.4256 25.3377 21.1601 25.3377 20.8466V12.9053C25.3377 12.6105 25.4507 12.345 25.6764 12.1101C25.9026 11.8748 26.1676 11.7572 26.472 11.7572C26.7764 11.7572 27.0369 11.8703 27.2539 12.0959C27.4704 12.3221 27.5789 12.5922 27.5789 12.9053V20.8607Z" fill="#565656" />
            <path d="M31.647 18.4827V20.7376C31.647 21.042 31.5363 21.3048 31.3147 21.5263C31.0936 21.7479 30.8308 21.8582 30.5264 21.8582C30.222 21.8582 29.9593 21.7479 29.7377 21.5263C29.5161 21.3048 29.4058 21.0329 29.4058 20.7101V12.935C29.4058 12.6027 29.5184 12.3239 29.7446 12.0978C29.9702 11.8721 30.2449 11.759 30.5676 11.759H33.1961C34.238 11.759 35.0867 12.0726 35.7417 12.6997C36.3963 13.3269 36.7241 14.1435 36.7241 15.1483C36.7241 16.1444 36.4146 16.9496 35.7971 17.5626C35.1791 18.176 34.3584 18.4827 33.3344 18.4827H31.647ZM31.647 13.765V16.5179H33.0716C33.4314 16.5179 33.745 16.3843 34.0123 16.1169C34.2801 15.8492 34.4138 15.531 34.4138 15.162C34.4138 14.7748 34.287 14.4452 34.0334 14.1728C33.7793 13.9009 33.4639 13.765 33.0853 13.765H31.647Z" fill="#565656" />
            <path d="M52.8772 42.0598C52.494 41.5379 51.7603 41.4253 51.2379 41.8085C50.7161 42.1916 50.6035 42.9259 50.9871 43.4477C52.6836 45.7581 53.9667 48.2918 54.8122 50.9697C52.3018 48.3939 48.577 46.2502 44.0204 44.794C43.8995 44.4159 43.775 44.0405 43.6441 43.6716C42.2227 39.6771 40.2681 36.3982 37.9555 34.1052C37.9669 34.091 37.9788 34.0764 37.9903 34.0622C40.508 34.8743 42.8806 36.0626 45.0517 37.6044C45.2577 37.7509 45.4948 37.8209 45.7297 37.8209C46.0968 37.8209 46.458 37.6492 46.6869 37.3274C47.0618 36.7992 46.9377 36.0672 46.4095 35.6923C44.2813 34.1812 41.976 32.98 39.537 32.1098C43.3946 27.0872 46.6045 21.6206 46.6045 16.6054C46.6045 7.44919 39.1557 0 30 0C20.8443 0 13.3955 7.44919 13.3955 16.6054C13.3955 20.1732 15.0275 24.2999 18.3842 29.2213C19.0485 30.195 19.7534 31.1591 20.479 32.1066C15.3488 33.9409 10.7657 37.2794 7.44141 41.6359C3.64655 46.609 1.64062 52.554 1.64062 58.8272C1.64062 59.4749 2.16568 60 2.81296 60H57.1866C57.8343 60 58.3594 59.4749 58.3594 58.8272C58.3594 52.7422 56.4638 46.9441 52.8772 42.0598ZM41.2733 44.025C39.4542 43.5841 37.5284 43.2472 35.5179 43.0257C35.2904 41.5942 34.5085 40.3102 33.3673 39.4441C34.3639 38.3231 35.4057 37.1407 36.449 35.9129C38.4023 37.9019 40.0443 40.7034 41.2733 44.025ZM15.7407 16.6054C15.7407 8.74237 22.1375 2.34512 30 2.34512C37.8625 2.34512 44.2593 8.74237 44.2593 16.6054C44.2593 23.6911 36.1588 32.7859 30.7983 38.8037C30.5251 39.1104 30.2591 39.4089 30.0005 39.7005C29.7505 39.4189 29.4937 39.1306 29.2305 38.8348C23.8586 32.7992 15.7407 23.6783 15.7407 16.6054ZM26.6345 39.4446C25.4942 40.3102 24.7128 41.5938 24.4853 43.0257C22.473 43.2468 20.5463 43.5841 18.7257 44.0254C19.9562 40.7007 21.5996 37.8973 23.5551 35.9079C24.6089 37.1516 25.6517 38.3372 26.6345 39.4446ZM13.9119 57.6549H4.08371C4.76761 53.5551 8.99689 49.8619 15.2051 47.5534C14.4319 50.733 13.992 54.1521 13.9119 57.6549ZM5.22766 50.9285C7.75406 43.0728 13.9467 36.66 22.0226 34.0604C22.0326 34.0727 22.0422 34.0846 22.0523 34.097C19.736 36.3899 17.7791 39.6712 16.3564 43.6688C16.225 44.0387 16.1 44.415 15.9787 44.7945C11.4468 46.2428 7.73712 48.371 5.22766 50.9285ZM28.8272 57.6549H16.2566C16.3509 53.7675 16.9139 50.0313 17.861 46.6855C19.9557 46.0899 22.2212 45.6413 24.6107 45.3703C25.1559 47.3804 26.786 48.9244 28.8277 49.3579V57.6549H28.8272ZM30.3305 47.1185C30.1598 47.1359 29.9881 47.1391 29.8174 47.1295C28.1163 47.0343 26.7613 45.6207 26.7613 43.8963C26.7613 42.8027 27.3175 41.7961 28.1987 41.2042C28.5168 41.5622 28.8245 41.9101 29.1188 42.2452C29.3413 42.4988 29.6626 42.6443 30 42.6443C30.3374 42.6443 30.6587 42.4988 30.8812 42.2452C31.1755 41.9096 31.4841 41.5613 31.8022 41.2033C32.6848 41.7957 33.2414 42.8027 33.2414 43.8963C33.2414 44.3289 33.1522 44.7643 32.9837 45.1625C32.5314 46.2222 31.5294 46.994 30.3374 47.1176C30.3351 47.1176 30.3328 47.1181 30.3305 47.1185C30.3328 47.1181 30.2829 47.1231 30.3305 47.1185C30.3328 47.1181 30.1598 47.1359 30.3305 47.1185ZM31.1728 57.6549V49.3579C33.1485 48.9381 34.7388 47.4783 35.3325 45.5626C35.3375 45.547 35.3416 45.531 35.3462 45.5154C35.3609 45.4674 35.3755 45.4193 35.3888 45.3703C37.7788 45.6413 40.0443 46.0895 42.1385 46.685C43.0861 50.0313 43.6491 53.768 43.7434 57.6549H31.1728ZM46.0881 57.6549C46.008 54.1521 45.5676 50.733 44.7945 47.5529C51.0027 49.8619 55.2324 53.5547 55.9163 57.6549H46.0881Z" fill="#565656" />
            <path d="M30 28.3341C23.6407 28.3341 18.4676 23.1605 18.4676 16.8012C18.4676 10.4402 23.6407 5.26514 30 5.26514C36.3606 5.26514 41.5356 10.4402 41.5356 16.8012C41.5356 23.1605 36.3606 28.3341 30 28.3341ZM30 7.6098C24.9339 7.6098 20.8127 11.7329 20.8127 16.8012C20.8127 21.8673 24.9339 25.989 30 25.989C35.0679 25.989 39.1905 21.8673 39.1905 16.8012C39.1905 11.7329 35.0679 7.6098 30 7.6098V7.6098Z" fill="#565656" />
            <path d="M49.2224 40.7776C48.8786 40.7776 48.5376 40.627 48.306 40.3372L48.2927 40.3208C47.8885 39.8149 47.9704 39.077 48.4758 38.6724C48.9816 38.2677 49.7195 38.3501 50.1242 38.8555L50.1375 38.8724C50.5417 39.3778 50.4598 40.1157 49.9544 40.5203C49.7383 40.6934 49.4792 40.7776 49.2224 40.7776Z" fill="#565656" />
            <defs>
              <clipPath id="clip0">
                <rect width="60" height="60" fill="white" />
              </clipPath>
            </defs>
          </svg>
        </div>
        <input type="text" placeholder="IP-address" onChange={(event) => changeIP(event.target.value)} />
      </div>
      <div className="Connecting-input">
        <div className="SVG-container">
          <svg viewBox="0 0 58 61" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M51 14.6129C51 14.6129 51.3166 32.613 43.3166 32.6129C35.3166 32.6128 29 32.6129 29 32.6129" stroke="#565656" strokeWidth="3" />
            <path d="M7.31659 14.6129C7.31659 14.6129 7 32.613 15 32.6129C23 32.6128 29.3166 32.6129 29.3166 32.6129" stroke="#565656" strokeWidth="3" />
            <circle cx="29.5" cy="53.5" r="6" stroke="#565656" strokeWidth="3" />
            <circle cx="29.5" cy="7.5" r="6" stroke="#565656" strokeWidth="3" />
            <circle cx="51" cy="10" r="4.5" stroke="#565656" strokeWidth="3" />
            <line x1="29.5" y1="47" x2="29.5" y2="14" stroke="#565656" strokeWidth="3" />
            <circle cx="7" cy="10" r="4.5" stroke="#565656" strokeWidth="3" />
          </svg>
        </div>
        <input type="text" placeholder="Port number" onChange={(event) => changePort(event.target.value)} />
      </div>
      <button className="Connect-button" type="button" onClick={() => connectWebsocket(ipPart, portPart)} onKeyDown={() => connectWebsocket(ipPart, portPart)}>
        {isLoading ? 'connecting' : 'connect'}
      </button>
      {isLoading
        ? (
          <div className="SVG-loader">
            <svg className="spinner" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
              <rect className="spinner__rect" x="0" y="0" width="100" height="100" fill="none" />
              <circle className="spinner__circle" cx="50" cy="50" r="40" stroke="#999999" fill="none" strokeWidth="6" strokeLinecap="round" />
            </svg>
          </div>
        )
        : (
          <h1 className="Error-message">
            {' '}
            {errorMsg}
            {' '}
          </h1>
        ) }
    </div>
  );
}

ConnectingPanel.defaultProps = {
  connectWebsocket: () => {},
  errorMsg: '',
  isLoading: false,
};

ConnectingPanel.propTypes = {
  connectWebsocket: PropTypes.func,
  errorMsg: PropTypes.string,
  isLoading: PropTypes.bool,
};