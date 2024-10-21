describe('Excluir receita', () => {
    it('Excluindo a receita com sucesso', () => {
        cy.visit('/');
        cy.get('#username').type('cypress')
        cy.get('#password').type('123abc')
        cy.get('button').click()
        cy.get('.card').click()
        cy.get('#nome').type('chocolate quente')
        cy.get('#ingredientes').type('Chocolate e leite integral.')
        cy.get('#modo_preparo').type('Aqueça o leite, acrescente o chocolate e misture bem.')
        cy.get('#comentarios').type('Bom para tomar no frio.')
        cy.get('.button').click()
        cy.get('h2').last().invoke('text').should('have.string', "chocolate quente")
        cy.get('h2').last().then(($el) => {
            const text = $el.text();
            expect(text).to.contain("chocolate quente");
            $el.click();
        });
        cy.get('.delete-btn').click()
    })

    it('cenario2', () => {
        //steps do cenario2
    })

    it('cenario3', () => {
        //steps do cenario3
    })
})