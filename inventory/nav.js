// nav.js — injects sidebar + topbar
function getPage(){return window.location.pathname.split('/').pop()||'dashboard.html';}
function navItem(href,label,iconPath,badge=''){
  const pg=getPage();
  const active=pg===href?'active':'';
  const bdg=badge?`<span class="nav-badge">${badge}</span>`:'';
  return `<a href="${href}" class="nav-item ${active}"><svg viewBox="0 0 24 24" fill="currentColor">${iconPath}</svg>${label}${bdg}</a>`;
}
function injectNav(topTitle,topSub=''){
  document.querySelector('link[data-shared]') || (() => {
    const l=document.createElement('link');l.rel='stylesheet';l.href='shared.css';l.dataset.shared='1';document.head.appendChild(l);
  })();
  const sidebar=`
  <aside class="sidebar">
    <div class="sb-logo">
      <div class="sb-logo-row">
        <div class="sb-icon"><svg viewBox="0 0 24 24" fill="white"><path d="M21 7L12 2L3 7V17L12 22L21 17V7ZM12 4.23L19 8.15V15.85L12 19.77L5 15.85V8.15L12 4.23Z"/></svg></div>
        <div><div class="sb-title">Inventory System</div><div class="sb-sub">Warehouse Management</div></div>
      </div>
    </div>
    <nav class="sb-nav">
      <div class="sb-section">Overview</div>
      ${navItem('dashboard.html','Dashboard','<rect x="2" y="3" width="9" height="9" rx="1"/><rect x="13" y="3" width="9" height="9" rx="1"/><rect x="2" y="14" width="9" height="7" rx="1"/><rect x="13" y="14" width="9" height="7" rx="1"/>')}
      <div class="sb-section">Inventory</div>
      ${navItem('receiving.html','Receiving Items','<path d="M20 6H4L2 2H22L20 6ZM4 8L6 22H18L20 8H4ZM15 11V19H13V11H15ZM11 11V19H9V11H11Z"/>','3')}
      ${navItem('inventory.html','Inventory System','<path d="M21 7L12 2L3 7V17L12 22L21 17V7ZM12 4.23L19 8.15V15.85L12 19.77L5 15.85V8.15L12 4.23Z"/>')}
      ${navItem('workorder.html','Work Orders','<path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM19 19H5V5H19V19ZM7 10H9V17H7V10ZM11 7H13V17H11V7ZM15 13H17V17H15V13Z"/>','5')}
      ${navItem('issuance.html','Issuance Form','<path d="M14 2H6C4.9 2 4 2.9 4 4V20C4 21.1 4.9 22 6 22H18C19.1 22 20 21.1 20 20V8L14 2ZM18 20H6V4H13V9H18V20ZM9 13H15V15H9V13ZM9 16H15V18H9V16ZM9 10H12V12H9V10Z"/>')}
      <div class="sb-section">Account</div>
      ${navItem('account.html','My Account','<path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V20H20V18C20 15.34 14.67 14 12 14Z"/>')}
      ${navItem('signin.html','Sign Out','<path d="M17 7L15.59 8.41L18.17 11H8V13H18.17L15.59 15.58L17 17L22 12L17 7ZM4 5H12V3H4C2.9 3 2 3.9 2 5V19C2 20.1 2.9 21 4 21H12V19H4V5Z"/>')}
    </nav>
    <div class="sb-footer">
      <div class="avatar">AJ</div>
      <div><div class="av-name">Alex Johnson</div><div class="av-role">Inventory Manager</div></div>
    </div>
  </aside>`;
  const topbar=`
  <header class="topbar">
    <div style="flex:1"><span class="topbar-title">${topTitle}</span>${topSub?`<span class="topbar-sub">— ${topSub}</span>`:''}</div>
    <div style="display:flex;gap:10px;align-items:center;">
      <div class="search-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg><input placeholder="Search..."></div>
      <button class="btn btn-secondary" style="gap:5px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:13px;height:13px;"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>3</button>
      <div class="avatar" style="cursor:pointer;">AJ</div>
    </div>
  </header>`;
  document.body.insertAdjacentHTML('afterbegin',sidebar);
  document.querySelector('.main').insertAdjacentHTML('afterbegin',topbar);
}
