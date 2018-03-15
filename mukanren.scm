(define (var n) n)

(define (var? n) (number? n))

(define (ext-s x v s)
  `((,x . ,v) . ,s))

(define (find u s)
  (let ((pr (assv u s)))
    (if pr (find (cdr pr) s) u)))

(define (unify u v s)
  (let ((u (find u s)) (v (find v s)))
    (cond ((eqv? u v) s)
          ((var? u) (ext-s u v s))
          ((var? v) (ext-s v u s))
          ((and (pair? u) (pair? v))
           (let ((s (unify (car u) (car v) s)))
             (and s (unify (cdr u) (cdr v) s))))
          (else #f))))

(define ((call/fresh f) S/c)
  (let ((S (car S/c)) (c (cdr S/c)))
    ((f (var c)) `(,S . ,(+ 1 c)))))

(define ($append $₁ $₂)
  (cond ((null? $₁) $₂)
        ((promise? $₁)
         (delay/name ($append $₂ (force $₁))))
        (else
         (cons (car $₁) ($append (cdr $₁) $₂)))))

(define ($append-map g $)
  (cond ((null? $) `())
        ((promise? $)
         (delay/name ($append-map g (force $))))
        (else ($append (g (car $))
                       ($append-map g (cdr $))))))

(define ((disj g₁ g₂) S/c) ($append (g₁ S/c) (g₂ S/c)))

(define ((conj g₁ g₂) S/c) ($append-map g₂ (g₁ S/c)))

(define (pull $) (if (promise? $) (pull (force $)) $))

(define (take n $)
  (cond ((null? $) '())
        ((and n (zero? (- n 1))) (list (car $)))
        (else (cons (car $)
                    (take (and n (- n 1))
                          (pull (cdr $)))))))

(define (call/initial-state n g)
  (take n (pull (g '(() . 0)))))

(define-syntax-rule (define-relation (rid . args) g)
  (define ((rid . args) S/c) (delay/name (g S/c))))
