(function () {
    'use strict'

    const LAST_UPDATED_ELEMENT_SELECTOR = '.js-whitepaper-last-updated'
    const PDF_LINK_SELECTOR = '.js-whitepaper-pdf-link'

    const lastUpdatedMessage = (date) => `Last updated: ${formatDate(date)}`

    const formatDate = (date) => {
        const format = new Intl.DateTimeFormat('en-CH', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        })

        return format.format(date)
    }

    const lastUpdatedElement = document.querySelector(LAST_UPDATED_ELEMENT_SELECTOR)
    const pdfLink = document.querySelector(PDF_LINK_SELECTOR)

    fetch(pdfLink.href, { method: 'HEAD', mode: 'cors', credentials: 'omit' })
        .then((response) => {
            const date = new Date(Date.parse(response.headers.get('last-modified')))
            const textNode = document.createTextNode(lastUpdatedMessage(date))
            lastUpdatedElement.appendChild(textNode)
        })
})()
