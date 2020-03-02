set number relativenumber
set autoindent
syntax on

set splitright
set splitbelow
set clipboard=unnamedplus

highlight LineNr ctermfg=grey

let fortran_have_tabs=1
au BufNewFile,BufRead *.py
    \ set tabstop=4 expandtab
au BufNewFile,BufRead *.tex
    \ set syntax=context

set background=dark
colorscheme gruvbox

hi Normal ctermbg=none 
hi EndOfBuffer ctermbg=none ctermfg=243 
hi LineNr ctermbg=none 
hi FoldColumn ctermbg=none

set scrolloff=10
