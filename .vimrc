set number
set autoindent
syntax on

set splitright
set splitbelow
set clipboard=unnamedplus


highlight LineNr ctermfg=grey

let fortran_have_tabs=1
au BufNewFile,BufRead *.py
    \ set tabstop=4 expandtab
