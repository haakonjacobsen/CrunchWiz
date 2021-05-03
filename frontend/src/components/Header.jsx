import React from 'react';
import './Header.css';

const Header = () => (
  <header className="App-header">
    <div className="Logo-wrapper">
      <svg width="93" height="85" viewBox="0 0 93 85" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fillRule="evenodd" clipRule="evenodd" d="M92.2558 50.8318H0.743896V51.258C0.743896 51.7093 1.10913 52.0771 1.55915 52.0771H1.61703C1.56567 52.236 1.5461 52.4031 1.59665 52.5686L8.32247 74.0704C8.43253 74.421 8.77983 74.6716 9.1255 74.643C9.49073 74.6315 9.80379 74.3776 9.89183 74.0213L14.8119 54.0594L20.1004 60.229C20.2643 60.4198 20.5113 60.5206 20.7583 60.5132C21.0094 60.5009 21.241 60.3739 21.3853 60.1675L21.7603 59.6302L23.7242 65.9095C23.8008 66.1545 24.0161 66.3142 24.2859 66.3109C24.5419 66.3019 24.7612 66.1241 24.8224 65.876L27.339 55.6624L34.7431 65.6458C34.9095 65.8702 35.1736 65.9931 35.4581 65.9726C35.7369 65.9505 35.9848 65.7875 36.116 65.5393L40.3643 57.5095L42.2182 60.0103C42.3356 60.1667 42.519 60.247 42.7196 60.2388C42.9144 60.2232 43.0881 60.1094 43.1802 59.9365L44.4756 57.4874L56.9848 77.3346C57.284 77.808 58.0642 77.808 58.3618 77.3346L62.747 70.377L69.6865 84.542C69.8234 84.8221 70.1071 84.9999 70.4169 84.9999H70.421C70.7341 84.9983 71.017 84.8172 71.1515 84.5346L80.3605 65.2133L82.212 69.0615C82.3506 69.3507 82.6498 69.5341 82.9636 69.5243C83.2824 69.5178 83.5678 69.3244 83.6941 69.0296L90.7599 52.6472C90.839 52.4629 90.8447 52.2614 90.7876 52.0763H91.439C91.889 52.0763 92.2543 51.7101 92.2543 51.2572C92.2553 51.1834 92.2557 50.994 92.2558 50.8318ZM24.2028 63.6135L26.4569 54.4689L27.0464 52.0755H20.5936L22.5869 58.4474L24.2028 63.6135ZM29.925 52.0755L32.3553 54.9121L34.342 52.0755H29.925ZM42.5956 58.5981L43.7737 56.3709L46.0458 52.0755H37.7588L40.957 56.3889L42.5956 58.5981ZM74.6652 58.1337L75.9362 60.7745L79.688 52.0755H48.9823L58.2729 66.8114L61.4051 61.8434C61.5152 61.6673 61.71 61.5666 61.9179 61.5764C62.1242 61.5887 62.3084 61.7107 62.3989 61.8967L67.1869 71.6704L73.6372 58.1353C73.7317 57.9362 73.9307 57.8093 74.1508 57.8093H74.1516C74.3709 57.8093 74.5698 57.9354 74.6652 58.1337Z" fill="#565656" />
        <path fillRule="evenodd" clipRule="evenodd" d="M91.4406 32.9244C91.8907 32.9244 92.2559 33.2914 92.2559 33.7435C92.2559 33.7891 92.2559 33.8793 92.2558 33.98H0.743896V33.7435C0.743896 33.2914 1.10913 32.9244 1.55915 32.9244H2.21053C2.15265 32.7393 2.15917 32.537 2.23825 32.3535L9.30404 15.9712C9.4304 15.6771 9.71656 15.4838 10.0353 15.4772C10.3484 15.4666 10.6476 15.6509 10.7862 15.94L12.6376 19.7882L21.8483 0.465259C21.9828 0.182663 22.2665 0.00163824 22.5788 0H22.5829C22.8935 0 23.1772 0.177749 23.3141 0.457887L30.2527 14.6221L34.638 7.6653C34.9364 7.19103 35.7166 7.19103 36.0149 7.6653L48.5242 27.5125L49.8204 25.0634C49.9125 24.8897 50.0862 24.7759 50.2802 24.7603C50.4808 24.7521 50.6634 24.8324 50.7816 24.9896L52.6347 27.4896L56.8829 19.4598C57.015 19.2116 57.2628 19.0486 57.5417 19.0273C57.8262 19.0068 58.0903 19.1297 58.2566 19.3541L65.6608 29.3383L68.1774 19.1248C68.2386 18.8757 68.4579 18.698 68.7139 18.6898C68.9837 18.6865 69.1981 18.8463 69.2756 19.0912L71.2387 25.3697L71.6145 24.8332C71.758 24.6268 71.9904 24.499 72.2415 24.4867C72.4885 24.4785 72.7363 24.5793 72.8994 24.7709L78.1879 30.9413L83.1088 10.9795C83.196 10.6231 83.5099 10.3692 83.8743 10.3577C84.2191 10.3299 84.5664 10.5805 84.6773 10.9311L91.4031 32.433C91.4537 32.5976 91.4341 32.7647 91.3836 32.9244H91.4406ZM68.797 21.3855L66.5429 30.531L65.9526 32.9236H72.4062L70.4129 26.5517L68.797 21.3855ZM63.0748 32.9236L60.6445 30.087L58.6577 32.9236H63.0748ZM50.4041 26.4026L49.2261 28.629L46.9532 32.9244H55.2418L52.0428 28.6118L50.4041 26.4026ZM18.3338 26.8662L17.0636 24.2254L13.3118 32.9253H44.0166L34.7268 18.1877L31.5946 23.1565C31.4846 23.3317 31.2897 23.4325 31.0819 23.4227C30.8756 23.4112 30.6922 23.2892 30.6009 23.1032L25.8129 13.3295L19.3618 26.8646C19.2672 27.0636 19.0675 27.1906 18.8482 27.1906H18.8474C18.6289 27.1906 18.4291 27.0645 18.3338 26.8662Z" fill="#565656" />
        <path d="M4.31337 48.0513C3.69004 48.0513 3.12337 47.8983 2.61337 47.5923C2.1147 47.275 1.71804 46.8557 1.42337 46.3343C1.1287 45.813 0.981371 45.2293 0.981371 44.5833L0.998371 39.2793C0.998371 38.656 1.14004 38.0893 1.42337 37.5793C1.71804 37.058 2.1147 36.6443 2.61337 36.3383C3.12337 36.021 3.69004 35.8623 4.31337 35.8623C4.9367 35.8623 5.4977 36.0153 5.99637 36.3213C6.49504 36.6273 6.8917 37.041 7.18637 37.5623C7.48104 38.0723 7.62837 38.6447 7.62837 39.2793V40.0613C7.62837 40.1067 7.6057 40.1293 7.56037 40.1293H5.65637C5.61104 40.1293 5.58837 40.1067 5.58837 40.0613V39.2793C5.58837 38.9053 5.4637 38.5823 5.21437 38.3103C4.97637 38.0383 4.67604 37.9023 4.31337 37.9023C3.90537 37.9023 3.5937 38.044 3.37837 38.3273C3.16304 38.5993 3.05537 38.9167 3.05537 39.2793V44.5833C3.05537 45.0027 3.17437 45.3427 3.41237 45.6033C3.6617 45.864 3.96204 45.9943 4.31337 45.9943C4.67604 45.9943 4.97637 45.8527 5.21437 45.5693C5.4637 45.2747 5.58837 44.946 5.58837 44.5833V43.8013C5.58837 43.756 5.61104 43.7333 5.65637 43.7333H7.57737C7.6227 43.7333 7.64537 43.756 7.64537 43.8013V44.5833C7.64537 45.2293 7.49237 45.813 7.18637 46.3343C6.8917 46.8557 6.49504 47.275 5.99637 47.5923C5.4977 47.8983 4.9367 48.0513 4.31337 48.0513ZM8.9565 47.8813C8.91116 47.8813 8.8885 47.853 8.8885 47.7963L8.9225 36.1173C8.9225 36.072 8.94516 36.0493 8.9905 36.0493H12.4245C13.0365 36.0493 13.5975 36.2023 14.1075 36.5083C14.6288 36.803 15.0425 37.2053 15.3485 37.7153C15.6545 38.214 15.8075 38.7807 15.8075 39.4153C15.8075 39.8347 15.7452 40.2143 15.6205 40.5543C15.4958 40.883 15.3485 41.1663 15.1785 41.4043C15.0085 41.631 14.8555 41.801 14.7195 41.9143C15.3315 42.5943 15.6375 43.3933 15.6375 44.3113L15.6545 47.7963C15.6545 47.853 15.6262 47.8813 15.5695 47.8813H13.6485C13.6032 47.8813 13.5805 47.8643 13.5805 47.8303V44.3113C13.5805 43.9033 13.4332 43.552 13.1385 43.2573C12.8552 42.9513 12.5038 42.7983 12.0845 42.7983H10.9625L10.9455 47.7963C10.9455 47.853 10.9228 47.8813 10.8775 47.8813H8.9565ZM10.9625 40.7583H12.4245C12.7758 40.7583 13.0875 40.628 13.3595 40.3673C13.6315 40.1067 13.7675 39.7893 13.7675 39.4153C13.7675 39.0527 13.6315 38.741 13.3595 38.4803C13.0988 38.2197 12.7872 38.0893 12.4245 38.0893H10.9625V40.7583ZM20.2177 48.0513C19.617 48.0513 19.0617 47.8983 18.5517 47.5923C18.0417 47.275 17.6337 46.8557 17.3277 46.3343C17.033 45.813 16.8857 45.2407 16.8857 44.6173L16.9197 36.1173C16.9197 36.072 16.9423 36.0493 16.9877 36.0493H18.8917C18.937 36.0493 18.9597 36.072 18.9597 36.1173V44.6173C18.9597 45.0027 19.0787 45.3313 19.3167 45.6033C19.566 45.864 19.8663 45.9943 20.2177 45.9943C20.5803 45.9943 20.8807 45.864 21.1187 45.6033C21.368 45.3313 21.4927 45.0027 21.4927 44.6173V36.1173C21.4927 36.072 21.5153 36.0493 21.5607 36.0493H23.4647C23.51 36.0493 23.5327 36.072 23.5327 36.1173L23.5667 44.6173C23.5667 45.252 23.4137 45.83 23.1077 46.3513C22.813 46.8727 22.4107 47.2863 21.9007 47.5923C21.402 47.8983 20.841 48.0513 20.2177 48.0513ZM25.062 47.8813C24.9713 47.8813 24.926 47.8417 24.926 47.7623L24.909 36.1853C24.909 36.0947 24.9543 36.0493 25.045 36.0493H26.575L29.448 42.7473L29.363 36.1853C29.363 36.0947 29.414 36.0493 29.516 36.0493H31.199C31.267 36.0493 31.301 36.0947 31.301 36.1853L31.318 47.7793C31.318 47.8473 31.2897 47.8813 31.233 47.8813H29.737L26.796 41.6253L26.915 47.7453C26.915 47.836 26.864 47.8813 26.762 47.8813H25.062ZM35.9227 48.0513C35.2994 48.0513 34.7327 47.8983 34.2227 47.5923C33.7241 47.275 33.3274 46.8557 33.0327 46.3343C32.7381 45.813 32.5907 45.2293 32.5907 44.5833L32.6077 39.2793C32.6077 38.656 32.7494 38.0893 33.0327 37.5793C33.3274 37.058 33.7241 36.6443 34.2227 36.3383C34.7327 36.021 35.2994 35.8623 35.9227 35.8623C36.5461 35.8623 37.1071 36.0153 37.6057 36.3213C38.1044 36.6273 38.5011 37.041 38.7957 37.5623C39.0904 38.0723 39.2377 38.6447 39.2377 39.2793V40.0613C39.2377 40.1067 39.2151 40.1293 39.1697 40.1293H37.2657C37.2204 40.1293 37.1977 40.1067 37.1977 40.0613V39.2793C37.1977 38.9053 37.0731 38.5823 36.8237 38.3103C36.5857 38.0383 36.2854 37.9023 35.9227 37.9023C35.5147 37.9023 35.2031 38.044 34.9877 38.3273C34.7724 38.5993 34.6647 38.9167 34.6647 39.2793V44.5833C34.6647 45.0027 34.7837 45.3427 35.0217 45.6033C35.2711 45.864 35.5714 45.9943 35.9227 45.9943C36.2854 45.9943 36.5857 45.8527 36.8237 45.5693C37.0731 45.2747 37.1977 44.946 37.1977 44.5833V43.8013C37.1977 43.756 37.2204 43.7333 37.2657 43.7333H39.1867C39.2321 43.7333 39.2547 43.756 39.2547 43.8013V44.5833C39.2547 45.2293 39.1017 45.813 38.7957 46.3343C38.5011 46.8557 38.1044 47.275 37.6057 47.5923C37.1071 47.8983 36.5461 48.0513 35.9227 48.0513ZM40.5659 47.8813C40.5205 47.8813 40.4979 47.853 40.4979 47.7963L40.5149 36.1173C40.5149 36.072 40.5432 36.0493 40.5999 36.0493H42.4869C42.5435 36.0493 42.5719 36.072 42.5719 36.1173L42.5549 40.7413H45.1049V36.1173C45.1049 36.072 45.1275 36.0493 45.1729 36.0493H47.0599C47.1165 36.0493 47.1449 36.072 47.1449 36.1173L47.1789 47.7963C47.1789 47.853 47.1505 47.8813 47.0939 47.8813H45.1899C45.1332 47.8813 45.1049 47.853 45.1049 47.7963V42.7983H42.5549V47.7963C42.5549 47.853 42.5322 47.8813 42.4869 47.8813H40.5659ZM50.1302 47.8813C50.0849 47.8813 50.0566 47.853 50.0452 47.7963L48.0392 36.1173C48.0279 36.072 48.0449 36.0493 48.0902 36.0493H49.9942C50.0396 36.0493 50.0679 36.072 50.0792 36.1173L51.1672 43.8013L52.2892 36.1173C52.3006 36.072 52.3346 36.0493 52.3912 36.0493H53.9212C53.9666 36.0493 53.9949 36.072 54.0062 36.1173L55.1112 43.8013L56.2162 36.1173C56.2276 36.072 56.2559 36.0493 56.3012 36.0493H58.1882C58.2449 36.0493 58.2676 36.072 58.2562 36.1173L56.2332 47.7963C56.2219 47.819 56.2049 47.8417 56.1822 47.8643C56.1596 47.8757 56.1482 47.8813 56.1482 47.8813H54.0912C54.0572 47.8813 54.0289 47.853 54.0062 47.7963L53.1392 41.6933L52.2722 47.7963C52.2609 47.853 52.2326 47.8813 52.1872 47.8813H50.1302ZM59.3426 47.8813C59.286 47.8813 59.2576 47.853 59.2576 47.7963L59.2746 36.1173C59.2746 36.072 59.2973 36.0493 59.3426 36.0493H61.2466C61.292 36.0493 61.3146 36.072 61.3146 36.1173L61.3316 47.7963C61.3316 47.853 61.309 47.8813 61.2636 47.8813H59.3426ZM62.368 47.8813C62.3113 47.8813 62.283 47.853 62.283 47.7963L62.3 45.9433L66.465 37.9873H62.521C62.4756 37.9873 62.453 37.9647 62.453 37.9193V36.1343C62.453 36.0777 62.4756 36.0493 62.521 36.0493H68.675C68.7316 36.0493 68.76 36.0777 68.76 36.1343V37.9703L64.612 45.8923H68.709C68.7543 45.8923 68.777 45.9207 68.777 45.9773L68.794 47.7963C68.794 47.853 68.7656 47.8813 68.709 47.8813H62.368ZM69.122 47.7963L71.23 36.1173C71.2414 36.072 71.2697 36.0493 71.315 36.0493H73.78C73.8254 36.0493 73.8537 36.072 73.865 36.1173L75.888 47.7963C75.8994 47.853 75.8767 47.8813 75.82 47.8813H73.933C73.8877 47.8813 73.8594 47.853 73.848 47.7963L73.661 46.5553H71.349L71.162 47.7963C71.1507 47.853 71.1224 47.8813 71.077 47.8813H69.19C69.1447 47.8813 69.122 47.853 69.122 47.7963ZM71.689 44.7363H73.321L72.624 39.9593L72.522 39.3303L72.454 39.9593L71.689 44.7363ZM77.0229 47.8813C76.9776 47.8813 76.9549 47.853 76.9549 47.7963L76.9889 36.1173C76.9889 36.072 77.0116 36.0493 77.0569 36.0493H80.4909C81.1029 36.0493 81.6639 36.2023 82.1739 36.5083C82.6952 36.803 83.1089 37.2053 83.4149 37.7153C83.7209 38.214 83.8739 38.7807 83.8739 39.4153C83.8739 39.8347 83.8116 40.2143 83.6869 40.5543C83.5622 40.883 83.4149 41.1663 83.2449 41.4043C83.0749 41.631 82.9219 41.801 82.7859 41.9143C83.3979 42.5943 83.7039 43.3933 83.7039 44.3113L83.7209 47.7963C83.7209 47.853 83.6926 47.8813 83.6359 47.8813H81.7149C81.6696 47.8813 81.6469 47.8643 81.6469 47.8303V44.3113C81.6469 43.9033 81.4996 43.552 81.2049 43.2573C80.9216 42.9513 80.5702 42.7983 80.1509 42.7983H79.0289L79.0119 47.7963C79.0119 47.853 78.9892 47.8813 78.9439 47.8813H77.0229ZM79.0289 40.7583H80.4909C80.8422 40.7583 81.1539 40.628 81.4259 40.3673C81.6979 40.1067 81.8339 39.7893 81.8339 39.4153C81.8339 39.0527 81.6979 38.741 81.4259 38.4803C81.1652 38.2197 80.8536 38.0893 80.4909 38.0893H79.0289V40.7583ZM85.2411 47.8813C85.1844 47.8813 85.1561 47.853 85.1561 47.7963L85.1901 36.1173C85.1901 36.072 85.2127 36.0493 85.2581 36.0493L88.4371 36.0323C89.0604 36.021 89.6271 36.1683 90.1371 36.4743C90.6584 36.7803 91.0721 37.194 91.3781 37.7153C91.6841 38.2253 91.8371 38.792 91.8371 39.4153V44.2943C91.8371 44.9517 91.6784 45.5523 91.3611 46.0963C91.0437 46.629 90.6187 47.054 90.0861 47.3713C89.5534 47.6887 88.9527 47.853 88.2841 47.8643L85.2411 47.8813ZM87.2301 45.7903H88.2841C88.7034 45.7903 89.0547 45.643 89.3381 45.3483C89.6327 45.0537 89.7801 44.7023 89.7801 44.2943V39.3983C89.7801 39.0357 89.6441 38.724 89.3721 38.4633C89.1114 38.1913 88.7997 38.061 88.4371 38.0723L87.2471 38.0893L87.2301 45.7903Z" fill="#565656" />
      </svg>
    </div>
    <div className="Device-status-nav">
      <div className="Device-status-wrapper">
        <div className="Device-logo">
          <svg width="53" height="53" viewBox="0 0 53 53" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g>
              <path d="M35.3349 1.77051C35.1176 0.725019 34.1859 -0.020282 33.1197 0.000420808H19.87C18.8038 -0.020282 17.8721 0.725019 17.6651 1.77051L15.895 9.0579H37.1568L35.3349 1.77051Z" fill="#424242" />
              <path d="M15.8433 43.9421L17.6548 51.2295C17.8721 52.275 18.7934 53.0203 19.8596 52.9996H33.1094C34.1756 53.0203 35.1072 52.275 35.3142 51.2295L37.0843 43.9421H15.8433Z" fill="#424242" />
              <rect x="11.2424" y="11.2424" width="30.5152" height="31.3182" rx="8" fill="#424242" />
              <ellipse cx="19.2728" cy="20.0758" rx="4.81818" ry="4.81818" fill="#313131" />
            </g>
            <defs>
              <clipPath id="clip0">
                <rect width="53" height="53" fill="white" />
              </clipPath>
            </defs>
          </svg>
        </div>
        <h2 className="Device-title">Empatica E4</h2>
      </div>
      <div className="Device-status-wrapper">
        <div className="Device-logo">
          {/* Icon made by Freepik from www.flaticon.com */}
          <svg width="63" height="63" viewBox="0 0 63 63" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g>
              <path d="M62.5296 30.2689C61.9673 29.6416 48.4414 14.8887 31.5001 14.8887C14.5587 14.8887 1.03292 29.6416 0.47047 30.2689C-0.156823 30.97 -0.156823 32.03 0.47047 32.7311C1.03292 33.3584 14.559 48.1113 31.5001 48.1113C48.4412 48.1113 61.9672 33.3584 62.5296 32.7311C63.1568 32.03 63.1568 30.97 62.5296 30.2689ZM31.5001 44.4199C24.3768 44.4199 18.5801 38.6233 18.5801 31.5C18.5801 24.3767 24.3768 18.5801 31.5001 18.5801C38.6234 18.5801 44.42 24.3767 44.42 31.5C44.42 38.6233 38.6234 44.4199 31.5001 44.4199Z" fill="#424242" />
              <path d="M33.3457 27.8086C33.3457 25.9518 34.2674 24.3184 35.6697 23.3137C34.4114 22.6695 33.0079 22.2715 31.5 22.2715C26.4116 22.2715 22.2715 26.4116 22.2715 31.5C22.2715 36.5884 26.4116 40.7285 31.5 40.7285C36.0557 40.7285 39.8263 37.4021 40.5713 33.0556C36.8545 34.2522 33.3457 31.4412 33.3457 27.8086Z" fill="#424242" />
            </g>
            <defs>
              <clipPath id="clip0">
                <rect width="63" height="63" fill="white" />
              </clipPath>
            </defs>
          </svg>
        </div>
        <h2 className="Device-title">Tobii</h2>
      </div>
      <div className="Device-status-wrapper">
        <div className="Device-logo">
          <svg width="53" height="53" viewBox="0 0 53 53" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g>
              <path d="M28.4182 5.41088C28.4182 2.42715 25.991 0 23.0077 0C20.0236 0 17.5964 2.42715 17.5964 5.41088C17.5964 8.39462 20.0236 10.8218 23.0077 10.8218C25.991 10.8218 28.4182 8.39428 28.4182 5.41088ZM19.9392 5.41088C19.9392 3.71904 21.3158 2.34281 23.0077 2.34281C24.6995 2.34281 26.0754 3.71904 26.0754 5.41088C26.0754 7.10272 24.6995 8.47896 23.0077 8.47896C21.3158 8.47896 19.9392 7.10239 19.9392 5.41088Z" fill="#424242" />
              <path d="M47.3441 21.9601C47.9315 21.6884 48.146 21.0096 47.9154 20.4052C42.4624 6.13782 20.363 13.8734 20.363 13.8734C19.7395 14.0398 19.368 14.679 19.5323 15.3029L24.1061 32.7066C24.244 33.2327 24.8086 33.6936 25.5362 33.542C26.1701 33.4094 26.5363 32.7374 26.3716 32.1119L22.0947 15.837C22.0947 15.837 40.5654 9.54091 45.7891 21.3892C46.0509 21.9809 46.7574 22.2312 47.3441 21.9601Z" fill="#424242" />
              <path d="M17.7638 17.1808C17.1172 17.1808 16.5924 17.7053 16.5924 18.3522C16.5924 20.9571 16.587 25.2809 8.29451 26.7017L7.29446 23.078C7.12243 22.4545 6.47816 22.089 5.85364 22.2604C5.23012 22.4334 4.86397 23.0773 5.036 23.7015L7.7068 33.38C7.85004 33.8998 8.26773 34.5246 9.07734 34.3633C9.92744 34.1946 10.1373 33.38 9.96526 32.7561L8.92071 28.9715C17.7735 27.3747 18.9352 22.4799 18.9352 18.3519C18.9352 17.7053 18.4114 17.1808 17.7638 17.1808Z" fill="#424242" />
              <path d="M26.9365 37.7928C29.594 37.2182 31.509 35.9313 32.6289 33.9667C34.5885 30.5285 33.3113 26.2776 33.1661 25.8244L30.7188 16.9562C30.5465 16.3324 29.9025 15.9666 29.2777 16.1386C28.6545 16.311 28.288 16.9556 28.4604 17.5794L30.9143 26.4727C30.9203 26.4908 30.925 26.5112 30.9317 26.5289C30.9431 26.5648 32.1008 30.1757 30.5883 32.816C29.8112 34.1719 28.4162 35.0758 26.4415 35.5026C23.8333 36.0669 21.9755 37.4009 20.9185 39.4693C18.405 44.3895 21.5488 51.6807 21.6833 51.9886C21.8761 52.4277 22.3262 53.0311 23.256 52.8019C24.1031 52.5927 24.088 51.6415 23.8293 51.0498C23.8005 50.9842 20.9962 44.4598 23.007 40.5309C23.7389 39.1021 25.0235 38.2068 26.9365 37.7928Z" fill="#424242" />
              <path d="M42.4446 50.6927C32.0282 47.8944 29.3068 40.235 29.1944 39.9037C28.9885 39.2929 28.3262 38.9629 27.7137 39.1664C27.0999 39.3709 26.7679 40.0349 26.9721 40.648C27.0962 41.0209 30.1509 49.8171 41.8358 52.9552C41.9386 52.9826 42.8877 53.2413 43.2713 52.1281C43.4832 51.5163 43.0695 50.8607 42.4446 50.6927Z" fill="#424242" />
            </g>
            <defs>
              <clipPath id="clip0">
                <rect width="53" height="53" fill="white" />
              </clipPath>
            </defs>
          </svg>
        </div>
        <h2 className="Device-title Device-active">openPose</h2>
      </div>
    </div>
  </header>
);

export default Header;
